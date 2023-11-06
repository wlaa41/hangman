# Hangman Game in Python WIP

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file)
- [Functions](#classes)
- [License](#license)

## Description
This project is a command-line version of the classic game Hangman, where the user guesses letters to try to infer a randomly selected word. It was developed to practice Python skills including handling user input, control structures, managing game state, and working with files.

What you'll find here:
- Implementation of the Hangman game logic in Python.
- User input validation and error handling.
- A simple and interactive command-line interface.

## Installation

Before you begin, ensure you have Python installed on your system.

1. Clone the repository:
```bash
git clone git@github.com:wlaa41/hangman.git
```
2. Run the script
```bash
python3 milestone_4.py
```


## Usage Instructions

This section explains how to play the Hangman game.

## How to Play

In this game, the computer selects a word at random from a given list, and you must try to guess the word one letter at a time. Be careful – you only have a limited number of guesses. Each incorrect guess brings the hangman closer to being fully drawn, and when the hangman is complete, the game is over, and you lose.

1. Start the game 

2. You will be prompted to enter a single-letter guess for the word.

3. Type your guess and press Enter.

4. The game will reveal whether your guess is correct or not.

5. If the guess is correct, the letter will be revealed in its correct position(s) within the word.
6. If the guess is incorrect, a part of the hangman will be drawn.
7. Continue guessing letters until you either complete the word or the hangman is fully drawn.

## Tips
. Think strategically about which letters you guess first.
. Remember common letters in the English language include vowels like 'a', 'e', 'i', 'o', 'u', as well as consonants like 't', 'n', 's', 'h', 'r', 'd', and 'l'.
. Keep track of the letters you've already guessed to avoid repeating them.

Good luck, and try not to hang the man!

## File Structure
hangman/
│
├── milestone_2.txt          - List of words to use in the game WIP
├── milestone_3.txt          - More encapsulated structure WIP
├── milestone_4.txt          - More encapsulated structure with a class and extra functions WIP
├── LICENSE            - License information
└── README.md          - Documentation for the project

## Classes and Functions

### `Hangman` Class

The `Hangman` class is the backbone of the game, encapsulating the game logic and state.

#### `__init__(self, word_list, num_lives=5)`
- **Description**: Initializes a new instance of the Hangman game.
- **Parameters**:
  - `word_list`: A list of strings, each representing a possible word to guess.
  - `num_lives`: An optional integer representing the number of incorrect guesses allowed before the game is lost (defaults to 5).
- **Attributes**:
  - `self.word`: A string randomly chosen from `word_list` that the player will guess.
  - `self.word_guessed`: A list of strings representing the letters of `self.word` that have been correctly guessed so far, with unguessed letters represented by underscores (`_`).
  - `self.num_letters`: An integer counting the number of unique letters in `self.word` that have yet to be guessed.
  - `self.list_of_guesses`: A list that will keep track of all the letters guessed by the player throughout the game.
- **Behavior**: When an object of `Hangman` is instantiated, it sets up the game by choosing a random word from the provided list, initializing the player's guessed word display to all underscores, and setting the remaining number of unique letters and lives.

#### `check_guess(self, guessed_letter)`
- **Description**: Evaluates the player's guessed letter and updates the game state accordingly.
- **Parameters**:
  - `guessed_letter`: A string representing the letter that the player has guessed.
- **Behavior**: When this method is called, it performs the following actions:
  1. Converts the guessed letter to lowercase (if necessary).
  2. Checks if the guessed letter is in the word to be guessed.
  3. If the guessed letter is correct, it updates `self.word_guessed` to reveal the letter's position(s) in the word.
  4. If the guessed letter is not correct, it decrements `self.num_lives` to indicate a lost life.
  5. Prints a message to the player informing them of the correctness of their guess and the remaining number of lives if the guess was incorrect.
  6. Once a letter is guessed correctly, it also decrements `self.num_letters`, which tracks how many more unique letters need to be guessed.

#### `ask_for_input(self)`
- **Description**: Requests and handles user input for letter guesses.
- **Parameters**: None.
- **Behavior**: This method is the interactive part of the game that prompts the user for input. It loops indefinitely, performing the following actions in each iteration:
  1. Prompts the user to enter a single-letter guess.
  2. Validates the input to ensure that exactly one alphabetic character is entered.
  3. If the input is invalid (either not a single character or not alphabetical), it informs the user and requests input again.
  4. Checks if the guessed letter has already been attempted and informs the user if so.
  5. If the input is a new valid letter, it proceeds to call `check_guess` with the user's guessed letter.
  6. Adds the guessed letter to `self.list_of_guesses` to keep track of all attempts.
  7. The loop continues until the word is fully guessed or the user runs out of lives.


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.

