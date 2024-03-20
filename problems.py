

problems = {
    "harry": """
Once upon a time there was a series of 5 books about a very English hero called Harry. (At least when this Kata was invented, there were only 5. Since then they have multiplied) Children all over the world thought he was fantastic, and, of course, so did the publisher. So in a gesture of immense generosity to mankind, (and to increase sales) they set up the following pricing model to take advantage of Harry's magical powers.
One copy of any of the five books costs 8 EUR. If, however, you buy two different books from the series, you get a 5% discount on those two books. If you buy 3 different books, you get a 10% discount. With 4 different books, you get a 20% discount. If you go the whole hog, and buy all 5, you get a huge 25% discount.
Note that if you buy, say, four books, of which 3 are different titles, you get a 10% discount on the 3 that form part of a set, but the fourth book still costs 8 EUR.
Potter mania is sweeping the country and parents of teenagers everywhere are queueing up with shopping baskets overflowing with Potter books. Your mission is to write a piece of code to calculate the price of any conceivable shopping basket, giving as big a discount as possible.
""",
    "fizzbuzz": """
    Imagine the scene. You are eleven years old, and in the five minutes before the end of the lesson, your Maths teacher decides he should make his class more “fun” by introducing a “game”. He explains that he is going to point at each pupil in turn and ask them to say the next number in sequence, starting from one. The “fun” part is that if the number is divisible by three, you instead say “Fizz” and if it is divisible by five you say “Buzz”. So now your maths teacher is pointing at all of your classmates in turn, and they happily shout “one!”, “two!”, “Fizz!”, “four!”, “Buzz!”… until he very deliberately points at you, fixing you with a steely gaze… time stands still, your mouth dries up, your palms become sweatier and sweatier until you finally manage to croak “Fizz!”. Doom is avoided, and the pointing finger moves on.

So of course in order to avoid embarassment infront of your whole class, you have to get the full list printed out so you know what to say. Your class has about 33 pupils and he might go round three times before the bell rings for breaktime. Next maths lesson is on Thursday. Get coding!

Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz “.

Sample output:

1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
... etc up to 100
""",
    "back_to_the_future": """
    L'équipe de production de Back to the Future voudrait remettre au goût du jour sa saga avec une technique marketing imparable :

Revenir dans le passé, en 2000 ! Et passer un deal super smart avec une boutique de vente de DVDs (vous vous rappelez encore ce que c'est on espère...) avec une promo qui déchire :

- le dvd d'un volet de la saga vaut 15€
- pour l'achat de 2 volets DIFFÉRENTS de la saga, on applique une réduction de 10% sur l'ensemble des DVDs "Back to the Future" achetés
- pour l'achat de 3 volets DIFFÉRENTS de la saga, on applique une réduction de 20% sur l'ensemble des DVDs "Back to the Future" achetés

La boutique de DVDs vend également d'autres films qui coûtent chacun 20€.

Portant la lourde responsabilité de réparer les failles temporelle, l'équipe de production vous charge d'écrire un programme qui aura le comportement suivant :

- En entrée, un panier sous forme de texte, séparé par des retours à la ligne qui contient le nom des films achetés
- En sortie, le nombre représentant le prix""",
    "bowling": """Create a program, which, given a valid sequence of rolls for one line of American Ten-Pin Bowling, produces the total score for the game. Here are some things that the program will not do:

    We will not check for valid rolls.
    We will not check for correct number of rolls and frames.
    We will not provide scores for intermediate frames.

Depending on the application, this might or might not be a valid way to define a complete story, but we do it here for purposes of keeping the kata light. I think you’ll see that improvements like those above would go in readily if they were needed for real.

We can briefly summarize the scoring for this form of bowling:

    Each game, or “line” of bowling, includes ten turns, or “frames” for the bowler.
    In each frame, the bowler gets up to two tries to knock down all the pins.
    If in two tries, he fails to knock them all down, his score for that frame is the total number of pins knocked down in his two tries.
    If in two tries he knocks them all down, this is called a “spare” and his score for the frame is ten plus the number of pins knocked down on his next throw (in his next turn).
    If on his first try in the frame he knocks down all the pins, this is called a “strike”. His turn is over, and his score for the frame is ten plus the simple total of the pins knocked down in his next two rolls.
    If he gets a spare or strike in the last (tenth) frame, the bowler gets to throw one or two more bonus balls, respectively. These bonus throws are taken as part of the same turn. If the bonus throws knock down all the pins, the process does not repeat: the bonus throws are only used to calculate the score of the final frame.
    The game score is the total of all frame scores.
"""
}

