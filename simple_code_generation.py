import os

import click
from openai import OpenAI

from problems import problems


TEST_FILE = "test_code_tdd.py"
CODE_FILE = "code_tdd.py"

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
DEEPSEEK_KEY = os.environ.get("DEEPSEEK_API_KEY")
clients = {
    "openai": OpenAI(api_key=OPENAI_API_KEY),
    "deepseek": OpenAI(api_key=DEEPSEEK_KEY, base_url="https://api.deepseek.com/v1")
}
models = {
    "openai": "gpt-4-1106-preview",
    "deepseek": "deepseek-coder",
}


@click.command()
@click.option("--problem-name")
@click.option("--model-name")
def main(problem_name: str, model_name: str):
    problem_description = problems[problem_name]
    model = models[model_name]
    client = clients[model_name]

    tests = generate_tests(problem_description, client, model)
    generate_code(tests, problem_description, client, model)


def generate_tests(problem_description: str, client: OpenAI, model: str):
    prompt = f"""
{problem_description}

Please generate a suite of tests to make sure that the code you are about to write is working as expected.

Please do not output the code to make the test pass.
Please make explicit the components of the expected result in the test. Here is an example of such a test :
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
    test = output.split("```python")[-1].split("```")[0]
    with open("test_code.py", "a") as f:
        f.write(test)
    return test


def generate_code(existing_tests: str, problem_description: str, client: OpenAI, model: str) -> str:
    prompt = f"""
{problem_description}

Here are the tests which have been written to check that the code is working as expected :
```python
{existing_tests}
```

Please output the code to make the tests pass.
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
    new_code = output.split("```python")[-1].split("```")[0]
    with open(CODE_FILE, "w") as f:
        f.write(new_code)
    return new_code


if __name__ == "__main__":
    main()
