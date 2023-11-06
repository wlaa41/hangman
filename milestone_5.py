import random

class Hangman:
    """A simple Hangman game class."""

    def __init__(self, word_list, num_lives=5):
        """Initialize the game with a list of words and a set number of lives."""

        self.word_list = word_list
        self.num_lives = num_lives
        self._word_to_guess= random.choice(self.word_list)
        self._word_guessed = ['_'] * len(self._word_to_guess)
        self.unique_letters_remained = len(set(self._word_to_guess))
        self._list_of_guesses=[]
    
    def _reduce_lives(self):
        """Reduce the number of lives left."""
        self.num_lives -= 1
        print(f"You have {self.num_lives} lives left.")
        
    def _update_word_guessed(self, guessed_letter):
        """Reveal the correctly guessed letters in the word."""
        for index, letter in enumerate(self._word_to_guess):
            if letter == guessed_letter:
                self._word_guessed[index] = letter
        self.unique_letters_remained -= 1
        
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
        guessed_letter = input('Guess a letter:')
        if self._is_valid_input(guessed_letter):
                self._check_guess(guessed_letter)
                self._list_of_guesses.append(guessed_letter)
                    
      
    
word_list = ['banana', 'apple', 'pear', 'orange', 'kiwi'] 

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list,num_lives)
    print(game._word_guessed)
    print(game.num_lives)
    print(game.unique_letters_remained)
    while True:
        print(f'trial ava = {game.num_lives}')
        print(f'unique letters ava = {game.unique_letters_remained}')
        if game.num_lives == 0:
            print('You lost!')
            break
        elif game.unique_letters_remained >0:
            game.ask_for_input()
            if game.unique_letters_remained ==0 :
                print('Congratulations. You won the game!')
                break
            
        
    
play_game(word_list)
