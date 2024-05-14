from hangman6.hangman641H import check_valid_input

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """ updates the list of old letters guessed with the new letter guessed.

    Args:
        letter_guessed: a string.
        old_letters_guessed: a list of strings.
    """
    valid = check_valid_input(letter_guessed, old_letters_guessed)
    letter_guessed = letter_guessed.lower()
    
    if (valid):
        old_letters_guessed.append(letter_guessed)
    else:
        old_letters_guessed.sort()
        print("X")
        print(" -> ".join(old_letters_guessed))
    return valid


# try_update_letter_guessed('b', ['b', 'c', 'd'])