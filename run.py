# Hangman Game
"""
Connection of run.py to Google Sheets spreadsheet.
Creation of variables to access Google Sheets.
"""
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("words")


def word_picker(level):
    """
    Randomly selects a word from the Google Sheets document,
    depending of difficulty setting.
    """
    from numpy import random
    choice = random.randint(SHEET.worksheet(level).cell(1, 2).value)
    word_choice = SHEET.worksheet(level).cell(choice, 1).value
    return word_choice.lower()


def choose_level():
    """
    Takes input from player to decide complication level of the game.
    """
    print("Level 1: Easy\n")
    print("Level 2: Medium\n")
    print("Level 3: Hard\n")
    level_choice = input("Choose a difficulty level (1,2 or 3)\n")
    if level_choice == "1":
        return "easy"
    elif level_choice == "2":
        return "medium"
    elif level_choice == "3":
        return "hard"
    else:
        print("Should be 1, 2 or 3 only!")
        choose_level()


def hidden_word_list(word):
    """
    Generates hidden word list from generated word.
    """
    hidden_list = []
    x = 1
    while x <= len(word):
        hidden_list.append("_")
        x += 1
    return hidden_list


def check_input(letter, word):
    """
    Checks input letter from player against word.
    Returns positions of the letter in the word or 0.
    """
    positions = [pos for pos, char in enumerate(word) if char == letter]
    if positions == []:
        return 0
    else:
        return positions


def play_game(word, hidden_letters):
    """
    Function to run the game.
    Takes input from the user and compares it to the generated word.
    Looks to compare guessed word against generated word.
    """
    word_list = list(word)
    guessed_letters = []
    img_hangman = 1
    while hidden_letters != word_list:
        print(SHEET.worksheet("hang").cell(1, img_hangman).value)
        print()
        print(hidden_letters)
        print()
        print(f"Wrong guesses: {guessed_letters}\n")
        letter = input("Guess a letter...\n")
        guess = check_input(letter, word)
        print()
        if guess == 0:
            print(f"Sorry, the word doesn't contain the letter {letter}\n")
            guessed_letters.append(letter)
            if img_hangman == 7:
                print(SHEET.worksheet("hang").cell(1, 8).value)
                print()
                print(f"You lost! The word was '{word}'\n")
                print("Try again!\n")
                main()
            img_hangman += 1
        else:
            for pos in guess:
                hidden_letters[pos] = letter
    print(f"You won! The word was '{word}'\n")
    main()


def main():
    """
    Primary function. Runs repeatedly.
    Generates a word and hidden clue and run's the game.
    """
    print("Lets play Hangman!\n")
    print(SHEET.worksheet("hang").cell(1, 8).value)
    print("\n")
    level = choose_level()
    word = word_picker(level)
    hidden_letters = hidden_word_list(word)
    play_game(word, hidden_letters)


main()
