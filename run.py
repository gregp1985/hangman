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

"""
Global variables
"""
player_name = ""
current_wins = 0
current_losses = 0
used_words = []


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


def check_used_already(letter, guessed):
    """
    Checks letter has not already been used.
    """
    if letter in guessed:
        return 2
    else:
        return 1


def valid_input(letter, guessed):
    """
    Checks that input character is alphabetical.
    """
    if letter.isalpha() and len(letter) == 1:
        result = check_used_already(letter, guessed)
        return result
    elif len(letter) > 1:
        return 3
    else:
        return 0


def check_input(letter, word, guessed):
    """
    Checks input letter from player against word.
    Returns positions of the letter in the word or 0.
    """
    letter.lower()
    validation = valid_input(letter, guessed)
    positions = [pos for pos, char in enumerate(word) if char == letter]
    if validation == 0:
        return "x"
    elif validation == 1:
        if positions == []:
            return 0
        else:
            return positions
    elif validation == 2:
        return "xx"
    elif validation == 3:
        return "xxx"


def update_score(score):
    """
    Updates global variables current_wins and current_losses
    to keep a running tally.
    """
    global current_wins
    global current_losses
    if score == 1:
        current_wins += 1
    else:
        current_losses += 1
    print(f"Wins: {current_wins} Losses: {current_losses}")


def generate_word(level):
    """
    Generates randomly chosen word dependent on difficulty level choice
    and runs the game.
    """
    global used_words
    print(f"Words so far: {used_words}\n")
    level_cap = level.capitalize()
    print(f"Difficulty level: {level_cap}\n")
    if used_words != []:
        level_change = input("Change Level? Y/N\n")
        print()
        if level_change.lower() == "y":
            level = choose_level()
    word = word_picker(level)
    if word in used_words:
        generate_word(level)
    else:
        used_words.append(word)
    hidden_letters = hidden_word_list(word)
    play_game(level, word, hidden_letters)


def play_game(level, word, hidden_letters):
    """
    Function to run the game.
    Takes input from the user and compares it to the generated word.
    Looks to compare guessed word against generated word.
    """
    global player_name
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
        guess = check_input(letter, word, guessed_letters)
        print()
        if guess == "x":
            print(f"{letter} is not a letter!\n")
        elif guess == "xx":
            print(f"You have already tried {letter}!")
        elif guess == "xxx":
            print("Too many characters! Enter 1 letter at a time!")
        elif guess == 0:
            print(f"Sorry, the word doesn't contain the letter {letter}\n")
            guessed_letters.append(letter)
            if img_hangman == 7:
                print(SHEET.worksheet("hang").cell(1, 8).value)
                print()
                print(f"Sorry {player_name} you lost! The word was '{word}'\n")
                print("Try again!\n")
                update_score(0)
                generate_word(level)
            img_hangman += 1
        else:
            for pos in guess:
                hidden_letters[pos] = letter
            print(f"Yep '{letter}' is in the word!")
    print(f"Well done {player_name} you won! The word was '{word}'\n")
    update_score(1)
    generate_word(level)


def main():
    """
    Primary function. Runs repeatedly.
    Generates a word and hidden clue and run's the game.
    """
    global player_name
    print("Lets play Hangman!\n")
    print(SHEET.worksheet("hang").cell(1, 8).value)
    print("\n")
    player_name = input("Enter your name:\n")
    print()
    print(f"Thanks {player_name}. What level do you want to play at?\n")
    level = choose_level()
    generate_word(level)


main()
