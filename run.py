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


def play_game(word):
    word_list = word.split()
    hidden_list = []
    x = 1
    while x <= len(word):
        hidden_list.append("_")
        x += 1
    print(hidden_list)

def main():
    print("Lets play Hangman!\n")
    print(SHEET.worksheet("hang").cell(1, 7).value)
    print("\n")
    level = choose_level()
    word = word_picker(level)
    play_game(word)


play_game("testing")
