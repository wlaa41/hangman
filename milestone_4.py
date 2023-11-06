import random

class Hangman:
    """A simple Hangman game class."""

    def __init__(self, word_list, num_lives=5):
        """Initialize the game with a list of words and a set number of lives."""

        self.word_list = word_list
        self._num_lives = num_lives
        self._word_to_guess= random.choice(self.word_list)
        self._word_guessed = ['_'] * len(self._word_to_guess)
        self._unique_letters = len(set(self._word_to_guess))
        self._list_of_guesses=[]
    
    def _reduce_lives(self):
        """Reduce the number of lives left."""
        self._num_lives -= 1
        print(f"You have {self._num_lives} lives left.")
        
    def _update_word_guessed(self, guessed_letter):
        """Reveal the correctly guessed letters in the word."""
        for index, letter in enumerate(self._word_to_guess):
            if letter == guessed_letter:
                self._word_guessed[index] = letter
        self._unique_letters -= 1
        
    def _is_valid_input(self, guessed_letter):
        """Validate the user's input."""
        if len(guessed_letter) != 1 or not guessed_letter.isalpha():
            print('Invalid input. Please, enter a single alphabetical character.')
            return False
        if guessed_letter in self._list_of_guesses:
            print("You already tried that letter!")
            return False
        return True
        
    def _check_guess(self, guessed_letter):
        """Check if the guessed letter is in the word and update the game state."""
        if guessed_letter.lower() in self._word_to_guess:
            print(f"Good guess! {guessed_letter} is in the word.")
            self._update_word_guessed(guessed_letter)
            print(self._word_guessed)
        else:
            print(f"Sorry, {guessed_letter} is not in the word.")
            self._reduce_lives()
            
    def ask_for_input(self):
        """Work in progress"""
        while True:
            guessed_letter = input('Guess a letter:')
            if self._is_valid_input(guessed_letter):
                    self._check_guess(guessed_letter)
                    self._list_of_guesses.append(guessed_letter)
      
    
word_list = ['banana', 'apple', 'pear', 'orange', 'kiwi'] 
word_lives = 5
Hang = Hangman(word_list,word_lives)
print(Hang._word_guessed)
print(Hang._num_lives)
print(Hang._unique_letters)
Hang.ask_for_input()