def longest(my_list):
    """ finds the longest string in a list of strings.

    Args:
        my_list (list): a list of strings.

    Returns:
        str: the longest string in the list.
    """
    my_list.sort(key=len, reverse=True)
    
    return my_list[0]

list1 = ["111", "234", "2000", "goru", "birthday", "09"]
print(longest(list1))