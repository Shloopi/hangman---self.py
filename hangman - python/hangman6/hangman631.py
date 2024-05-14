def are_lists_equal(list1, list2):
    """ checks if the lists contain the same elements.

    Args:
        list1 (_type_): a float and integer list.
        list2 (_type_): a float and integer list.
    """
    is_equal = len(list1) == len(list2) # check if the lists are of the same length
    if is_equal:
        # sort the lists.
        list1.sort()
        list2.sort()

        is_equal = (list1 == list2) # check if the lists are equal.
        
    return is_equal

list1 = [0.6, 1, 2, 3]
list2 = [3, 2, 0.6, 1]
list3 = [9, 0, 5, 10.5]
print(are_lists_equal(list1, list2))
print(are_lists_equal(list1, list3))