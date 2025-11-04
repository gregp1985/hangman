![hangman logo](/assets/images/hangman.png)

This hangman game is a Python terminal game, which runs in the Code Institute mock terminal on Heroku

Players can choose different levels of difficulty and play to guess the randomly chosen word. Easy 4-5 letters, Medium 6-7 letters and Hard 8-9 letters.

[Here is the live version of my project](https://hangmangame-534861d8daf1.herokuapp.com/)

![Site Mockup]()

## How to Play

This hangman game is the classic guess the word letter by letter. 

Every incorrect guess is recorded and an additional part of the hangman image is added to the image (7 in total).

If the player wins or loses the game this is recorded and they can play again. The score is tallied at the beginning of each round.

The word is presented as under scores representing letters and are replaced with correct guesses.

Incorrect guesses result in the hangman image being created and incorrect letters are added to the wrong guess list.

![Wins / Losses]()

## Features

- Difficulty Settings
    - Easy (4-5 letters)
    - Medium (6-7 letters)
    - Hard (8-9 letters)
![Difficulty settings]()
- Words randomly selected from list of hundreds of different words
    - Words selected at random dependent of difficulty
    - Words cannot be repeated in the game cycle
- Word is represented by underscores to hide it from the player
- Scores are tallied as part of the game cycle
![Score Tally]()
- Validation in place to stop "non" letters and repeat letters from being selected
![Validation]()

## Future Feature

- Add complexity with multiple word phrases
- Addtion of a timed game facility to compete against others and give statistics

## Data Model



## Testing