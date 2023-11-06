import random

word_list = ['banana', 'apple', 'pear', 'orange', 'kewi']
print(word_list)
word = random.choice(word_list)

def check_guess(guess_letter):
    """
    Check if the guessed letter is in the word and provide feedback to the user.

    Parameters:
    guess_letter (str): The letter that the user has guessed.

    Returns:
    None

    This function converts the guess to lowercase, checks if the guess is in the word,
    and prints a message to the console to inform the user whether their guess was correct or not.
    """
    if guess_letter.lower() in word:
        print(f"Good guess! {guess_letter} is in the word.")
    else:
        print(f"Sorry, {guess_letter} is not in the word. Try again.")
        
def ask_for_input():
    """
    Repeatedly prompt the user to guess a letter until they enter a valid single alphabetical character.

    Parameters:
    None

    Returns:
    None

    This function uses a while loop to continuously prompt the user for input until a valid guess is received.
    It ensures that the input is a single alphabetic character and, once valid input is received, passes it to
    the check_guess function.
    """
    while True:
        guess_letter = input('Guess a letter:')
        if len(guess_letter) ==1 and guess_letter.isalpha():
            break
        else:
            print('Invalid letter. Please, enter a single alphabetical character.')
    check_guess(guess_letter)
        
ask_for_input()