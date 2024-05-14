def is_valid_input(guessed_letter):
    """returns True if the guessed letter is a single letter and is an alphabet letter, False otherwise.

    Args:
        guessed_letter (char): a letter guessed by the user.

    Returns:
        boolean: True if the guessed letter is a single letter and is an alphabet letter, False otherwise.
    """
    return len(guessed_letter) == 1 and guessed_letter.isalpha()



print(is_valid_input('a'))
print(is_valid_input('A'))
print(is_valid_input('$'))
print(is_valid_input("ab"))
print(is_valid_input("app$"))