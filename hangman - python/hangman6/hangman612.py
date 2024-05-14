def shift_left(my_list):
    """ return a list with the first element moved to the end of the list.

    Args:
        my_list (list): a list with 3 elements.

    Returns:
        list - 3 arguments: return a list with the first element moved to the end of the list.
    """
    my_list.append(my_list.pop(0))
    return my_list

print(shift_left([1, 2, 3]))