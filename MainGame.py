"""
CLI Hangman Game
A classic word guessing game played in the terminal.

Author: Your Name
"""

import random
import os
from words import WORD_LIST


# ASCII art for each stage of the hangman
HANGMAN_STAGES = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """,
]

MAX_WRONG_GUESSES = len(HANGMAN_STAGES) - 1  # 6 wrong guesses allowed


def clear_screen():
    """Clear the terminal screen (works on Windows, Mac, Linux)."""
    os.system("cls" if os.name == "nt" else "clear")


def choose_word():
    """Pick a random word from the word list."""
    return random.choice(WORD_LIST).lower()


def display_word(word, guessed_letters):
    """
    Show the word with dashes for unguessed letters.
    Example: 'python' with guessed 'p', 'n' → 'p _ _ _ _ n'
    """
    display = [letter if letter in guessed_letters else "_" for letter in word]
    return " ".join(display)


def get_guess(guessed_letters):
    """Get a valid letter guess from the user."""
    while True:
        guess = input("\n🔤 Guess a letter: ").lower().strip()

        if len(guess) != 1:
            print("⚠️  Please enter exactly ONE letter.")
        elif not guess.isalpha():
            print("⚠️  Please enter a letter (A-Z).")
        elif guess in guessed_letters:
            print(f"⚠️  You already guessed '{guess}'. Try a different letter.")
        else:
            return guess


def display_game_state(word, guessed_letters, wrong_guesses):
    """Show the current state of the game."""
    clear_screen()
    print("=" * 40)
    print("🎮  HANGMAN  🎮".center(40))
    print("=" * 40)
    print(HANGMAN_STAGES[wrong_guesses])
    print(f"Word:  {display_word(word, guessed_letters)}")
    print(f"\nGuessed letters: {', '.join(sorted(guessed_letters)) or 'None'}")
    print(f"Wrong guesses: {wrong_guesses} / {MAX_WRONG_GUESSES}")
    print("=" * 40)


def play_game():
    """Run one round of Hangman."""
    word = choose_word()
    guessed_letters = set()
    wrong_guesses = 0

    while True:
        display_game_state(word, guessed_letters, wrong_guesses)

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print(f"\n🎉 YOU WIN! The word was: '{word.upper()}'")
            return True

        # Check loss condition
        if wrong_guesses >= MAX_WRONG_GUESSES:
            print(f"\n💀 GAME OVER! The word was: '{word.upper()}'")
            return False

        # Get user's guess
        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in word:
            print(f"✅ Good guess! '{guess}' is in the word.")
        else:
            print(f"❌ Sorry, '{guess}' is not in the word.")
            wrong_guesses += 1


def play_again():
    """Ask the user if they want to play another round."""
    while True:
        answer = input("\n🔁 Play again? (y/n): ").lower().strip()
        if answer in ("y", "yes"):
            return True
        elif answer in ("n", "no"):
            return False
        else:
            print("⚠️  Please enter 'y' or 'n'.")


def show_welcome():
    """Display a welcome message."""
    clear_screen()
    print("=" * 40)
    print("🎮  WELCOME TO HANGMAN  🎮".center(40))
    print("=" * 40)
    print("\nRules:")
    print("  • Guess the hidden word one letter at a time.")
    print(f"  • You have {MAX_WRONG_GUESSES} wrong guesses before you lose.")
    print("  • Good luck!\n")
    input("Press ENTER to start...")


def main():
    """Main entry point for the game."""
    show_welcome()

    wins = 0
    losses = 0

    while True:
        won = play_game()
        if won:
            wins += 1
        else:
            losses += 1

        print(f"\n📊 Score — Wins: {wins} | Losses: {losses}")

        if not play_again():
            print("\n👋 Thanks for playing! Goodbye!")
            print(f"Final score — Wins: {wins} | Losses: {losses}\n")
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Game interrupted. Goodbye!")
