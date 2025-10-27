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
    from numpy import random
    choice = random.randint(SHEET.worksheet(level).cell(1, 2).value)
    word_choice = SHEET.worksheet(level).cell(choice, 1).value
    return word_choice.lower()


def choose_level():
    print("Level 1: Easy\n")
    print("Level 2: Medium\n")
    print("Level 3: Hard\n")
    level_choice = input("Choose a difficulty level (1,2 or 3)")
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
    hidden_list = []
    x = 1
    while x <= len(word):
        hidden_list.append("_")
        x += 1
    return hidden_list


def check_input(letter, word):
    positions = [pos for pos, char in enumerate(word) if char == letter]
    if positions == []:
        incorrect_guess(letter)
    else:
        correct_guess(word, positions)


def play_game(word, hidden_letters):
    print(hidden_letters)
    letter = input("Guess a letter...")
    check_input(letter, word)


def main():
    print("Lets play Hangman!\n")
    print(SHEET.worksheet("hang").cell(1, 7).value)
    print("\n")
    level = choose_level()
    word = word_picker(level)
    hidden_letters = hidden_word_list(word)
    play_game(word, hidden_letters)


test  = check_input("p", "class")
print(test)

