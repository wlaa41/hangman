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

### Personal Gain

#### The Unexpected Educational Value of a README
Crafting the Hangman game, I discovered that the simplicity of the code belies its educational value. It was through this process that I gained a profound appreciation for the README file. The revelation was not merely in mastering its creation, but in recognizing its systematic structure—a feature that now makes deciphering other READMEs more intuitive.

## Installation

Before you begin, ensure you have Python installed on your system.

1. Clone the repository:
```bash
git clone git@github.com:wlaa41/hangman.git
```
2. Run the script
```bash
python3 milestone_5.py
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
├── milestone_2.py          - Initial list of words for the game.
├── milestone_3.py          - Improved structure with additional functionality.
├── milestone_4.py          - Introduction of the Hangman class.
├── milestone_5.py          - Final game script, complete with all functionalities.
├── LICENSE                 - License information.
└── README.md               - Documentation for the project.
```

## Classes and Functions

### `Hangman` Class

The `Hangman` class is the backbone of the game, encapsulating the game logic and state.

#### Attributes

`word_list:` List of potential words to guess.
`num_lives:` Number of permitted incorrect guesses.
`_word_to_guess:` The current word to be guessed by the player.
`_word_guessed:` Representation of the guessed parts of the word.
`unique_letters_remained:` Count of distinct letters that need to be guessed.
`_list_of_guesses:` Record of all guessed letters.

These attributes are used to track the progress of the game, manage the game state, and determine the end conditions of the game.

### Class Methods

### `__init__(self, word_to_guess, num_lives=6)`
This method is the constructor for the Hangman game class. It initializes the game by setting the word that needs to be guessed and the number of lives the player has. The word is stored in a variable, typically represented by underscores for unguessed letters. The number of lives is set to a default of 6 but can be adjusted.

### `_reduce_lives(self)`
A private method that decrements the `num_lives` variable by one. This method is called whenever the player makes an incorrect guess.

#### `_update_word_guessed(self, letter)`
This private method updates the display of the word to be guessed with the correctly guessed letter. It replaces the appropriate underscores with the letter if the letter is found in the word.

#### `_is_valid_input(self, letter)`
A private method that checks if the player's input is valid. Validity checks usually include ensuring the input is a single letter and has not been guessed before.

#### `_check_guess(self, letter)`
This method checks the player's guessed letter against the word. If the letter is in the word, `_update_word_guessed` is called; otherwise, `_reduce_lives` is invoked.

#### `ask_for_input(self)`
This public method is used to prompt the player for their guess and process it. It calls `_is_valid_input` to validate the guess and then `_check_guess` to check if the guess is correct.

### Game Flow

#### `play_game(self)`
The `play_game` method is the core method that initializes the game loop and manages the rounds of guessing. It continues to ask the player for input until the word is guessed correctly or the player runs out of lives. The method also handles the end-of-game message, displaying whether the player won or lost.

#### Game Flow Steps:

1. **Initialize Game**: Set up the game with the word to guess and number of lives.
2. **Game Loop**: Repeat the following steps until the game ends:
    - Display the current state of the word to guess and the number of lives remaining.
    - Invoke `ask_for_input` to get the player's guess.
    - Check if the game has been won (all letters guessed) or lost (no lives remaining).
3. **End Game**: Once the loop ends, display an appropriate message to the player indicating a win or a loss, and reveal the word if not already guessed.

## Conclusion

Each method in the Hangman game class plays a specific role in managing the game's state and player interactions. Together, they create a seamless and engaging game experience for the player, maintaining the classic challenge of Hangman with the support of modern programming practices.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.

