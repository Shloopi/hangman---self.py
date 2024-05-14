def check_valid_input(letter_guessed, old_letters_guessed):
    """ checks if the letter guessed is valid.

    Args:
        letter_guessed (_type_): a string.
        old_letters_guessed (_type_): a list of strings.
    """
    # check if the letter guessed is a single letter, an alphabet letter and not guessed before.
    return len(letter_guessed) == 1 and letter_guessed.isalpha() and letter_guessed.lower() not in old_letters_guessed