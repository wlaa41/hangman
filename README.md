# Hangman Game in Python WIP

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file)
- [Classes and Functions](#classes)
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
```
hangman/
│
├── milestone_2.py          - List of words to use in the game WIP
├── milestone_3.py          - More encapsulated structure WIP
├── milestone_4.py          - More encapsulated structure with a class and extra functions WIP
├── LICENSE            - License information
└── README.md          - Documentation for the project
```

## Classes and Functions

### `Hangman` Class

The `Hangman` class is the backbone of the game, encapsulating the game logic and state.

#### Attributes

- `word_list`: A list of strings, each a possible word to guess.
- `_num_lives`: An integer representing the number of incorrect guesses allowed before the game is lost. Initialized by the `num_lives` parameter.
- `_word_to_guess`: A string representing the word that the player needs to guess. This is selected randomly from `word_list`.
- `_word_guessed`: A list of strings that represents the letters of the word that have been correctly guessed so far. Each unguessed letter is represented by an underscore `_`.
- `_unique_letters`: An integer counting the number of unique letters in `_word_to_guess` that have yet to be guessed.
- `_list_of_guesses`: A list that keeps track of all the letters the player has guessed throughout the game.

These attributes are used to track the progress of the game, manage the game state, and determine the end conditions of the game.


#### `__init__(self, word_list, num_lives=5)`
- **Behavior**: Initializes the game by selecting a random word from `word_list`, setting up the initial `word_guessed` with underscores, and initializing the number of lives and unique letters to be guessed. This method sets the stage for the game.

#### `_reduce_lives(self)`
- **Behavior**: Decreases the `_num_lives` by one whenever a player guesses incorrectly and informs the player of the remaining lives. This method controls the life-tracking aspect of the game, bringing the game closer to an end with each wrong guess.

#### `_update_word_guessed(self, guessed_letter)`
- **Behavior**: Reveals the correctly guessed letters in their respective positions within `_word_guessed`. It also reduces the count of `_unique_letters` by one for each newly guessed letter, moving the game towards a successful end.

#### `_is_valid_input(self, guessed_letter)`
- **Behavior**: Checks whether the player's input is valid, ensuring it is a single alphabetical character and not a repeat guess. It prompts the player to re-enter their guess if the input is invalid.

#### `_check_guess(self, guessed_letter)`
- **Behavior**: Determines if the guessed letter is in the `_word_to_guess`. If it is, it praises the player and updates the game state using `_update_word_guessed`. If not, it calls `_reduce_lives` to decrement the number of lives.

#### `ask_for_input(self)`
- **Behavior**: This method is a continuous loop that prompts the player to guess a letter and processes the input. It calls `_is_valid_input` to validate and `_check_guess` to process the guess. The loop persists until the word is fully guessed or the player runs out of lives.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.

