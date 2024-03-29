from typing import List, Optional
from print_color import print

import click
from openai import OpenAI

from debug import debug_code
from llm_config import clients, models
from problems import problems


TEST_FILE = "test_code_tdd.py"
CODE_FILE = "code_tdd.py"


@click.command()
@click.option("--problem-name")
@click.option("--model-name")
def main(problem_name: str, model_name: str):
    problem_description = problems[problem_name]
    model = models[model_name]
    client = clients[model_name]
    existing_tests = []
    code = ""
    with open("test_code_tdd.py", "w") as f:
        f.write("from code_tdd import *\n\n")


    new_test = generate_new_test(existing_tests, code, problem_description, client, model)
    code = generate_new_code(existing_tests, new_test, code, problem_description, client, model)
    existing_tests.append(new_test)

    iteration = 1
    while True:
        print(f"Starting iteration {iteration}")
        new_test = generate_new_test(existing_tests, code, problem_description, client, model)
        if not new_test:
            break
        new_code = generate_new_code(existing_tests, new_test, code, problem_description, client, model)
        if new_code == code:
            break
        code = new_code
        existing_tests.append(new_test)
        iteration += 1


def generate_new_test(existing_tests_list: List[str], existing_code: str,
                      problem_description: str, client: OpenAI, model: str) -> Optional[str]:
    existing_tests = "\n".join(existing_tests_list)
    if len(existing_tests) == 0:
        prompt = f"""
You are a skilled software developer, who loves writing code using Test Driven Development. You have been given the following problem to solve :

{problem_description}

We are going to solve this problem by using Test Driven Development. Please output the first test you can generate to solve part of this problem using TDD and pytest.

Please do not output the code to make the test pass.
Please make explicit the components of the expected result in the test. 
Each test should only test one case, and so have only one assertion.
Here is an example of such a test :
```python
def test_compute_number_of_eaten_apples():
    # Given
    number_of_people = 3
    number_of_days = 4
    apples_per_day = 1

    # When
    number_of_eaten_apples = compute_number_of_eaten_apples(number_of_people, number_of_days, apples_per_day)

    # Then
    assert number_of_eaten_apples = number_of_people * number_of_days * apples_per_day
"""
    else:
        prompt = f"""
You are a skilled software developer, who loves writing code using Test Driven Development. You have been given the following problem to solve :
{problem_description}

We are using Test Driven Development to solve this problem. Here are the current tests we have generated : 
```python
{existing_tests}
```

Here is the current state of our code :
```python
{existing_code}
```

Please output the simplest test you can add to improve the behavior of our code.

Please do not output the code to make the test pass.
Do not output the imports, as they are already written.

Please make explicit the components of the expected result in the test. 
Each test should only test one case, and so have only one assertion.
Here is an example of such a test :
```python
def test_compute_number_of_eaten_apples():
    # Given
    number_of_people = 3
    number_of_days = 4
    apples_per_day = 1

    # When
    number_of_eaten_apples = compute_number_of_eaten_apples(number_of_people, number_of_days, apples_per_day)

    # Then
    assert number_of_eaten_apples = number_of_people * number_of_days * apples_per_day
```

    If you think that the code is already complete and no new test is needed, please do not output any code.
    """

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model=model,
    )
    output = chat_completion.choices[0].message.content
    if "```python" not in output:
        return None
    new_test = output.split("```python")[-1].split("```")[0]
    print(new_test, color="magenta")

    if "test" in new_test:
        with open(TEST_FILE, "a") as f:
            f.write(new_test)
        return new_test
    else:
        return None


def generate_new_code(
        existing_tests_list: List[str], new_test: str, existing_code: str,
        problem_description: str, client: OpenAI, model: str
) -> str:
    existing_tests = "\n".join(existing_tests_list)
    if len(existing_tests) == 0:
        prompt = f"""
You are a skilled software developer. You have been given the following problem to solve :
{problem_description}

We are using Test Driven Development to solve this problem. Here is a first test which was generated : 
```python
{new_test}
```

Please output the simplest code to make this test pass.
Please output the whole code without any ellipsis, as it will be directly written to a file.
Do not output the imports, as they are already written. The tested module name is {CODE_FILE}.
"""
    else:
        prompt = f"""
{problem_description}

We are using Test Driven Development to solve this problem. 

Here are the first tests which were generated : 
```python
{existing_tests}
```

Here is the code which was generated to make the tests pass :
```python
{existing_code}
```

A new test has just been generated :
```python
{new_test}
```

Please make the simplest change to the code to make this test pass.
Do not try to modify the existing test suite.
Please output the whole code without any ellipsis, as it will be directly written to a file.
Do not output the imports, as they are already written. The tested module name is {CODE_FILE}.

If you think that no change is needed in the existing code to make the tests pass, just output the existing code.
"""
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model=model,
    )
    output = chat_completion.choices[0].message.content
    if "```python" not in output:
        return existing_code
    new_code = output.split("```python")[-1].split("```")[0]

    print(new_code, color="blue")

    with open(CODE_FILE, "w") as f:
        f.write(new_code)

    debug_code(TEST_FILE, CODE_FILE, problem_description, client, model, 3)
    return new_code


if __name__ == "__main__":
    main()
