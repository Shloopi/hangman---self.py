def numbers_letters_count(my_str):
    """_summary_

    Args:
        my_str (String): a string

    Returns:
        list: returns a list with the number of number 
        and number of non number characters in the string.
    """
    num_count = letter_count = 0
    
    for i in my_str: # for each character in the string
        if i.isdigit(): # if the character is a number.
            num_count += 1
        else: 
            letter_count += 1
    return [num_count, letter_count]


print(numbers_letters_count("Python 3.6.3"))
