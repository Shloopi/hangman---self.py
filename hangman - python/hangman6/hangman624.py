def extend_list_x(list_x, list_y):
    """ changes list_x so that it contains list_y at the begining.

    Args:
        list_x (list): a list.
        list_y (list): a list.
    """
    list_x[:0] = list_y
    
list_x = [1, 2, 3]
list_y = [-2, -1, 0]
print(list_x)
extend_list_x(list_x, list_y)
print(list_x)
