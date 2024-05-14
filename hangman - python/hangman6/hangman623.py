def format_list(my_list):
    my_list[-1] = 'and ' + str(my_list[-1]) # add 'and' before the last element
    return my_list[::2] + my_list[-1:] # returns a list with elements at the even indexes plus the last element.

print(format_list(["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]))
    