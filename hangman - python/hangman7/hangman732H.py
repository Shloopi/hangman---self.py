def check_win(secret_word, old_letters_guessed):
    """ this function checks if the player has won the game.

    Args:
        secret_word (String): the secret word.
        old_letters_guessed (list (char)): a list of letters guessed by the player.

    Returns:
        boolean: True if the player has won, False otherwise.
    """
    win = True
    i = 0
    
    # iterate through the secret word.
    while (win and i < len(secret_word)):
        # if the letter is not in the old letters guessed, the player has not won.
        win = secret_word[i] in old_letters_guessed
        i += 1
    
    return win


secret_word = "friends"
old_letters_guessed = ['m', 'p', 'j', 'i', 's', 'k']
print(check_win(secret_word, old_letters_guessed))

secret_word = "yes"
old_letters_guessed = ['d', 'g', 'e', 'i', 's', 'k', 'y']
print(check_win(secret_word, old_letters_guessed))

secret_word = "hangman"
old_letters_guessed = ['a', 'g', 'h', 'm', 'n']
print(check_win(secret_word, old_letters_guessed))