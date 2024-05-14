from hangman6.hangman641H import check_valid_input

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """ updates the list of old letters guessed with the new letter guessed.

    Args:
        letter_guessed: a string.
        old_letters_guessed: a list of strings.
    """
    # check if the letter is valid.
    valid = check_valid_input(letter_guessed, old_letters_guessed)
    
    # get the lower case version of the letter.
    letter_guessed = letter_guessed.lower()
    
    if (valid): # if the letter is valid.
        old_letters_guessed.append(letter_guessed) # append the letter to the list.
    else:
        # otherwise sort the list and print the letters in the list.
        old_letters_guessed.sort()
        print("\nguess in not valid.\nprevious guesses:")
        print(" -> ".join(old_letters_guessed))
    return valid


# try_update_letter_guessed('b', ['b', 'c', 'd'])