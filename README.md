![hangman logo](/assets/images/hangman.png)

This hangman game is a Python terminal game, which runs in the Code Institute mock terminal on Heroku

Players can choose different levels of difficulty and play to guess the randomly chosen word. Easy 4-5 letters, Medium 6-7 letters and Hard 8-9 letters.

[Here is the live version of my project](https://hangmangame-534861d8daf1.herokuapp.com/)

![Site Mockup](/assets/images/site-mockup.png)

## How to Play

This hangman game is the classic guess the word letter by letter. 

Every incorrect guess is recorded and an additional part of the hangman image is added (7 in total).

If the player wins or loses the game this is recorded and they can play again. The score is tallied at the beginning of each round.

The word is presented as under scores representing letters and are replaced with correct guesses.

Incorrect guesses result in the hangman image being created and incorrect letters being added to the wrong guess list.

![Wins / Losses](/assets/images/wins-losses.png)

## Features

- Hangman image is updated on each incorrect guess using preformatted images from the Google Sheets Document

![Google Sheets Hangman Images](/assets/images/google-sheets-hangman-images.png)

- Difficulty Settings (can be changed on each round)
    - Easy (4-5 letters)
    - Medium (6-7 letters)
    - Hard (8-9 letters)
    
![Difficulty settings](/assets/images/level-choices.png)
- Words randomly selected from list of hundreds of different words (currently residing on a spreadsheet in Google Sheets)
    - Words selected at random dependent on difficulty
    - Words cannot be repeated in the game cycle

![Google Sheets Easy Words](/assets/images/google-sheets-easy-words.png)

![Google Sheets Medium Words](/assets/images/google-sheets-medium-words.png)

![Google Sheets Hard Words](/assets/images/google-sheets-hard-words.png)

- Word is represented by underscores to hide it from the player
- Scores are tallied as part of the game cycle

![Wins / Losses](/assets/images/wins-losses.png)

- Validation in place to stop "non" letters, repeat letters and multiple letter entries from being inputted by the player

![NonAlpha](/assets/images/non-alpha.png)
![NonAlpha2](/assets/images/non-alpha-2.png)
![Multiple Characters](/assets/images/multiple-characters.png)
![Duplicate Characters](/assets/images/duplicate_character.png)

## Future Feature

- Add complexity with multiple word phrases
- Addition of a timed game facility to compete against others and give statistics

## Data Model

My model is based on functions and variables. Namely lists and objects.

User inputs for Name and Current Scores are kept globally. As is the used words list.

All other data is created and passed between functions, including the word and letter choices.

The word is turned into a list and a hidden list for the player to see. This is then used for comparison.

## Testing

Testing in file [TESTING.md](TESTING.md)

## Deployment

This project was deployed using Code Institute's mock terminal for Heroku.

- Steps for deployment:
    - Clone Repository
    - Create new Heroku App
    - Setup Config Vars (Port:8000 and CREDS for GoogleDocs)
    - Set the Buildpacks to Python and NodeJS in that order
    - Link the Heroku App to the Github repository
    - Click on Deploy

## Credits

- Code Institute for the deployment terminal
- Code Institute love-sandwiches project for the gspread and google auth imports and the links to connect to google sheets documents.
- [Byjus.com](https://byjus.com/english) for the lists of common words