![hangman logo](/assets/images/hangman.png)

This hangman game is a Python terminal game, which runs in the Code Institute mock terminal on Heroku

Players can choose different levels of difficulty and play to guess the randomly chosen word. Easy 4-5 letters, Medium 6-7 letters and Hard 8-9 letters.

[Here is the live version of my project](https://hangmangame-534861d8daf1.herokuapp.com/)

![Site Mockup]()

## How to Play

This hangman game is the classic guess the word letter by letter. 

Every incorrect guess is recorded and an additional part of the hangman image is added (7 in total).

If the player wins or loses the game this is recorded and they can play again. The score is tallied at the beginning of each round.

The word is presented as under scores representing letters and are replaced with correct guesses.

Incorrect guesses result in the hangman image being created and incorrect letters being added to the wrong guess list.

![Wins / Losses]()

## Features

- Difficulty Settings
    - Easy (4-5 letters)
    - Medium (6-7 letters)
    - Hard (8-9 letters)
![Difficulty settings]()
- Words randomly selected from list of hundreds of different words (currently residing on a spreadsheet in Google Sheets)
    - Words selected at random dependent on difficulty
    - Words cannot be repeated in the game cycle
![Google Sheets]()
- Word is represented by underscores to hide it from the player
- Scores are tallied as part of the game cycle
![Score Tally]()
- Validation in place to stop "non" letters, repeat letters and multiple letter entries from being inputted by the player
![Validation]()

## Future Feature

- Add complexity with multiple word phrases
- Addition of a timed game facility to compete against others and give statistics

## Data Model

My model is based on functions and variables. Namely lists and objects.

User inputs for Name and Current Scores are kept globally. As is the used words list.

All other data is created and passed between functions, including the word and letter choices.

The word is turned into a list and a hidden list for the player to see. This is then used for comparison.

## Testing

I have manually tested this project by doing the following:

- Passed the code through the PEP8 linter and confirmed no problems (PEP8online.com)
- Given invalid inputs (incorrect characters, duplicate characters, multiple characters) to confirm the expected output.
- Tested in my local terminal as well as the Code Institute Heroku terminal.

Further Testing in file [TESTING.md](TESTING.md)

## Bugs

### Solved Bugs

- Scores were not being updated each time but overwriting back to zero. Resolved by changing the variables to the global scope.
- Players were able to enter non alpha characters and multiple characters each time. Resolved with validation functions.

### Remaining Bugs

- No bugs remaining.

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