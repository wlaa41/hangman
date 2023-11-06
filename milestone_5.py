import random

class Hangman:
    """Hangman game class where users can guess the word one letter at a time."""

    def __init__(self, word_list, num_lives=5):
        """
        Initialize the Hangman game instance.

        Parameters:
        word_list (list): A list of words from which the game randomly selects one.
        num_lives (int): The number of lives the player starts with (default is 5).
        """
        self.word_list = word_list
        self.num_lives = num_lives
        self._word_to_guess= random.choice(self.word_list)
        self._word_guessed = ['_'] * len(self._word_to_guess)
        self.unique_letters_remained = len(set(self._word_to_guess))
        self._list_of_guesses=[]
    
    def _reduce_lives(self):
        """Reduce the number of lives by one and inform the player of their remaining lives."""
        self.num_lives -= 1
        print(f"You have {self.num_lives} lives left.")
        
    def _update_word_guessed(self, guessed_letter):
        """
        Update the word guessed list with the correctly guessed letter.

        Parameters:
        guessed_letter (str): The letter that the player has guessed.
        """
        # Reveal the positions of the correctly guessed letter in the word to guess.
        for index, letter in enumerate(self._word_to_guess):
            if letter == guessed_letter:
                self._word_guessed[index] = letter
        # Decrease the count of unique letters as one more is now guessed.
        self.unique_letters_remained -= 1
        
    def _is_valid_input(self, guessed_letter):
        """
        Check if the guessed letter is valid (a single alphabetical character not guessed before).

        Parameters:
        guessed_letter (str): The letter that the player has guessed.

        Returns:
        bool: True if the input is valid, False otherwise.
        """
        # Check if input is a single alphabetic character and not already guessed.
        if len(guessed_letter) != 1 or not guessed_letter.isalpha():
            print('Invalid input. Please, enter a single alphabetical character.')
            return False
        if guessed_letter in self._list_of_guesses:
            print("You already tried that letter!")
            return False
        return True
        
    def _check_guess(self, guessed_letter):
        """
        Check if the guessed letter is in the word. Update the word or reduce lives accordingly.

        Parameters:
        guessed_letter (str): The letter that the player has guessed.
        """
        # Convert to lowercase to ensure consistent comparison.
        if guessed_letter.lower() in self._word_to_guess:
            print(f"Good guess! {guessed_letter} is in the word.")
            self._update_word_guessed(guessed_letter)
            print(self._word_guessed)
        else:
            print(f"Sorry, {guessed_letter} is not in the word.")
            self._reduce_lives()
            
    def ask_for_input(self):
        """
        Asks the player for their next guess.
        """
        guessed_letter = input('Guess a letter:')
        # Proceed only if the input is valid.
        if self._is_valid_input(guessed_letter):
                self._check_guess(guessed_letter)
                self._list_of_guesses.append(guessed_letter)
                    
      
    

def play_game(word_list):
    """
    Play a round of the Hangman game with the given list of words.

    Parameters:
    word_list (list): A list of words to use for the Hangman game.
    """
    # Set the number of lives the player starts with.
    num_lives = 5
    # Create an instance of the Hangman game.
    game = Hangman(word_list,num_lives)
    
    # Main game loop
    while True:
        print()
        print('---------------------------------------')
        print(f'trial ava = {game.num_lives}')
        print(f'unique letters ava = {game.unique_letters_remained}')
        print(game._word_guessed)
        # Check for the lose condition.
        if game.num_lives == 0:
            print('---------------------------------------')
            print('---------------------------------------')
            print('---------------------------------------')
            print('You lost!')
            print('---------------------------------------')
            print('---------------------------------------')
            print('---------------------------------------')
            break
        
        # The player continues to guess as long as there are remaining unique letters.
        if game.unique_letters_remained >0:
            game.ask_for_input()
            if game.unique_letters_remained ==0 :
                print('---------------------------------------')
                print('---------------------------------------')
                print('---------------------------------------')
                print('Congratulations. You won the game!')
                print('---------------------------------------')
                print('---------------------------------------')
                print('---------------------------------------')
                break
            
        
word_list = ['banana', 'apple', 'pear', 'orange', 'kiwi'] 
play_game(word_list)
