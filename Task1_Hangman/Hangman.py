
import random

# List of five predefined words
words = ["python", "computer", "geography", "science", "program"]

# Randomly select a word
secret_word = random.choice(words)

# Variables
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

print("================================")
print("       WELCOME TO HANGMAN")
print("================================")
print("Guess the hidden word one letter at a time.")
print("You have 6 incorrect guesses allowed.\n")

# Main game loop
while incorrect_guesses < max_attempts:

    # Display the current word
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect guesses:", incorrect_guesses)
    print("Guessed letters:", guessed_letters)

    # Check if the player has won
    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You guessed the word:", secret_word)
        break

    # Get player's guess
    guess = input("\nEnter a letter: ").lower().strip()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one valid letter.")
        continue

    # Check repeated guesses
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Check whether the guess is correct
    if guess in secret_word:
        print("Correct guess!")
    else:
        incorrect_guesses += 1
        print("Wrong guess!")

# Check if the player lost
if incorrect_guesses == max_attempts:
    print("\nGame over! You have used all your attempts.")
    print("The correct word was:", secret_word)

print("\nThank you for playing Hangman!")
