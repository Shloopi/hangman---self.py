def last_early(my_str):
    return my_str[-1] in my_str[:-1] # true if last char is in the rest of the string


print(last_early("yey"))