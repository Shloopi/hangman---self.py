import os
from hangman9.hangman941H import choose_word
from hangman8.hangman841H import print_hangman
from hangman7.hangman731H import show_hidden_word
from hangman7.hangman732H import check_win
from hangman6.hangman642H import try_update_letter_guessed
from hangman2 import hangman251H


def get_input():
    """ this function gets a file's path that contains words
        and an index of a word in the file from the user.
    """
    valid = False
    
    while not valid:
        file_path = input("Enter the file path: ")
        
        # check if the file exists.
        valid = os.path.isfile(file_path)
        
        if not valid:
            print("Enter an existing file path.")
    
    valid = False

    while not valid:
        index = input("Enter the index of the word in the file: ")
        
        # check if the index a  number.
        valid = index.isdigit()

        if not valid:
            print("Enter a number.")
        
    
    return (file_path, int(index))

def check_lose(num_of_tries):
    """ this function checks if the player lost the game.
    """
    return num_of_tries == hangman251H.MAX_TRIES
    
def ask_for_a_guess(letters_guessed):
    """ this function asks the player for a guess and returns it.

    Args:
        letters_guessed (list (char)): a list of letters guessed by the player.

    Returns:
        char: a letter guessed by the player.
    """
    valid = False
    guess = ''
    while not valid:
        guess = input("Guess a letter: ")
        
        # check if the guess is valid.
        valid = try_update_letter_guessed(guess, letters_guessed)
    
    return guess.lower()

def game_over(secret_word, num_of_tries):
    """ this function prints the result of the game.

    Args:
        secret_word (String): the secret word.
        num_of_tries (int): the number of tries the player had.
    """
    # if the player lost the game.
    if (check_lose(num_of_tries)):
        print("LOSE\n")
    else:
        print("WIN in", str(num_of_tries), "tries.\n")
        
    print("The word was: " + secret_word)
    
def game_loop():
    """ this function is the main loop of the game.
    """
    # set initial variables.
    letters_guessed = []
    num_of_tries = 0
    guess = ''
    
    # print a welcome message.
    hangman251H.print_welcome_message()
    
    # get the file path and the index of the word from the user.
    file_path, index = get_input()
    
    # get the number of words in the file and the secret word.
    num_of_words, secret_word = choose_word(file_path, index)
    
    print("Let's start!\n")
    
    # print the state of the hangman.
    print_hangman(num_of_tries)
    
    # print the hidden word.
    print(show_hidden_word(secret_word, letters_guessed))
        
    # run as long as the game is not over.
    while not check_lose(num_of_tries) and not check_win(secret_word, letters_guessed):
        # ask the player for a guess.
        guess = ask_for_a_guess(letters_guessed)
        
        # if the guess is in the secret word.
        if guess in secret_word:
            # print the hidden word.
            print(show_hidden_word(secret_word, letters_guessed))
        # if the guess is not in the secret word.
        else:
            # increase the number of tries.
            num_of_tries += 1
            print(guess)
            
            # print the state of the hangman.
            print_hangman(num_of_tries)

    # print the result of the game.
    game_over(secret_word, num_of_tries)

def main():
    game_loop()
    
    
    
if __name__ == "__main__":
    main()

