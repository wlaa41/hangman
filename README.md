# Hangman Game in Python

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file)
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


# Usage Instructions

This section explains how to play the Hangman game.

## How to Play

In this game, the computer selects a word at random from a given list, and you must try to guess the word one letter at a time. Be careful – you only have a limited number of guesses. Each incorrect guess brings the hangman closer to being fully drawn, and when the hangman is complete, the game is over, and you lose.

1. Start the game 

1. You will be prompted to enter a single-letter guess for the word.

1. Type your guess and press Enter.

1. The game will reveal whether your guess is correct or not.

1. If the guess is correct, the letter will be revealed in its correct position(s) within the word.
1. If the guess is incorrect, a part of the hangman will be drawn.
1. Continue guessing letters until you either complete the word or the hangman is fully drawn.

## Tips
. Think strategically about which letters you guess first.
. Remember common letters in the English language include vowels like 'a', 'e', 'i', 'o', 'u', as well as consonants like 't', 'n', 's', 'h', 'r', 'd', and 'l'.
. Keep track of the letters you've already guessed to avoid repeating them.

Good luck, and try not to hang the man!

# File Structure
hangman/
│
├── milestone_2.txt          - List of words to use in the game
├── LICENSE            - License information
└── README.md          - Documentation for the project

# License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.

