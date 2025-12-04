![hangman logo](/assets/images/hangman.png)
# Testing

I have manually tested this project by doing the following:

- Passed the code through the PEP8 linter and confirmed no problems (https://pep8ci.herokuapp.com/)

![CI PEP8 Linter](/assets/images/ci-python-linter.png)

- Given invalid inputs (incorrect characters, duplicate characters, multiple characters) to confirm the expected output.
- Tested in my local terminal as well as the Code Institute Heroku terminal.

Below is documentation of further tests carried out on the hangman game.

## Multiple runs of the easy game
![Easy Game Multiple Plays](/assets/images/easy-multiple-plays.png)
## Multiple runs of the medium game
![Medium Game Multiple Plays](/assets/images/medium-multiple-plays.png)
## Multiple runs of the hard game
![Hard Game Multiple Plays](/assets/images/hard-multiple-plays.png)
## Incorrect character entries

- Non alpha character

![NonAlpha](/assets/images/non-alpha.png)
![NonAlpha2](/assets/images/non-alpha-2.png)

- Multiple characters

![Multiple Characters](/assets/images/multiple-characters.png)

- Duplicate character

![Duplicate Characters](/assets/images/duplicate_character.png)

## Change Level feature

Tested the change level feature multiple times and Scores and Used Words list reset on level change each time as designed.

## Bugs Encountered

### Solved Bugs

- User able to put correct letter in as capital and graded as incorrect entry, Corrected this by adding code to convert user input to lowercase before validation.

- User able to enter blank username. Resolved by adding validation (while loop) to check for this and produce exception until the user makes a valid entry.

- If user enters incorrect data multiple times when choosing the level a traceback error occured. Resolved by removing the code to rerun the function and implementing a while loop with a try/except function to validate the level choice.

- Scores were not being updated each time but overwriting back to zero. Resolved by changing the variables to the global scope.

- Players were able to enter non alpha characters and multiple characters each time. Resolved with validation functions.

### Remaining Bugs

- No bugs remaining.