"""A simple hangman game."""

import random
import requests


def play_game():
    """Play one round of hangman."""
    # To do: handle non-200 status codes and additional errors; pylint: disable=invalid-name
    try:
        # Make an API call and store the response.
        URL = 'https://www.mit.edu/~ecprice/wordlist.10000'
        r = requests.get(URL)

        # Store API response in a variable.
        words_list = r.text.strip().split("\n")
    except requests.exceptions.ConnectionError:
        print("The words list from the MIT website could not be retrieved.")
        quit()

    target_word = random.choice(words_list)

    # pylint: disable=invalid-name
    tries_left = 5
    game_ended = False
    revealed_letters = ["_" for char in target_word]
    bad_letters = set()
    VALID_CHARACTERS = "abcdefghijklmnopqrstuvwxyz"

    print("\nWelcome to HANGMAN. The word has been chosen. What is your first guess?")

    while game_ended is False:
        print('\n' + ''.join(revealed_letters))
        print(f'Tries left: {tries_left}')
        print("Bad letters: " + ', '.join(bad_letters))

        # pylint: disable=invalid-name
        guess = ""
        while guess not in VALID_CHARACTERS or len(guess) != 1 or guess in bad_letters:
            guess = input("Guess a letter: ").lower()

        if guess not in target_word:
            bad_letters.add(guess)
            tries_left -= 1
            if tries_left == 0:
                print("\nOof! Better luck next time!")
                print("The target word was " + target_word)
                game_ended = True
        else:
            for i, char in enumerate(target_word):
                if guess == char:
                    revealed_letters[i] = guess
                if ''.join(revealed_letters) == target_word:
                    print("\nThat's correct! You win!")
                    game_ended = True


play_game()

# pylint: disable=invalid-name
flag = False
while flag is False:
    response = ""
    while response != 'y' and response != 'n':
        response = input("\nPlay another round? (y/n)").lower()

    if response == 'y':
        play_game()
    else:
        flag = True
