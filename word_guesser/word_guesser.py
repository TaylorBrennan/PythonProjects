# pylint: disable=R1732

"Simple word guesser game in Python using external dictionary file."

import sys
import random

try:
    DICTIONARY = open("dict.txt", "r", encoding="UTF-8").read().splitlines()
except FileNotFoundError:
    print("[Error] Dictionary file not found")
    sys.exit(1)
RANDOM_WORD = random.choice(DICTIONARY).lower()

print("Welcome to the word guesser!")
print("I'm thinking of a word that is", len(RANDOM_WORD), "letters long.")
print("You have", 10, "guesses to get it.")

for x in range(10):
    guess = input("Guess a word: ").lower()
    if guess == RANDOM_WORD:
        print("You win!")
        print("The word was", RANDOM_WORD)
        sys.exit(0)
    else:
        print("Sorry, that's not in the word.")
        print("You have", 10 - (x+1), "guesses left.")
print("You lose!")
print("The word was", RANDOM_WORD)
print("Better luck next time!")
