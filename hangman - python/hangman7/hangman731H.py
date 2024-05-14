def show_hidden_word(secret_word, old_letters_guessed):
    """ this function returns the hidden word with the guessed letters revealed.

    Args:
        secret_word (String): the secret word.
        old_letters_guessed (list (char)): the list of the guessed letters.

    Returns:
        String: hidden word with the guessed letters revealed.
    """
    returned_word = "_ " * len(secret_word)
    
    # run for the letters in the secret word.
    for i in range(len(secret_word)):
        # if the letter is in the old letters guessed, replace the letter in the returned word.
        if secret_word[i] in old_letters_guessed:
            returned_word = returned_word[:i*2] + secret_word[i] + returned_word[i*2+1:]
            
    return returned_word

# secret_word = "mammals"
# old_letters_guessed = ['s', 'p', 'j', 'i', 'm', 'k']
# print(show_hidden_word(secret_word, old_letters_guessed))