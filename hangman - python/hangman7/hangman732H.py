def check_win(secret_word, old_letters_guessed):
    """_summary_

    Args:
        secret_word (String): the secret word.
        old_letters_guessed (list (char)): a list of letters guessed by the player.

    Returns:
        _type_: _description_
    """
    # if the length of the secret word is greater than the length of the old letters guessed, the player has not won.
    win = len(secret_word) <= len(old_letters_guessed)
    i = 0
    
    # iterate through the secret word.
    while (win and i < len(secret_word)):
        # if the letter is not in the old letters guessed, the player has not won.
        win = secret_word[i] in old_letters_guessed
        i += 1
    
    return win

# secret_word = "friends"
# old_letters_guessed = ['m', 'p', 'j', 'i', 's', 'k']
# print(check_win(secret_word, old_letters_guessed))

# secret_word = "yes"
# old_letters_guessed = ['d', 'g', 'e', 'i', 's', 'k', 'y']
# print(check_win(secret_word, old_letters_guessed))
 