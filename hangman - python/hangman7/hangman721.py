def is_greater(my_list, n):
    new_list = []
    for i in my_list: # for each element in my_list
        if i > n: # if the element is greater than n
            new_list.append(i) # append the element to new_list
            
    return new_list

print(is_greater([1, 30, 25, 60, 27, 28], 25)) # [30, 60, 27, 28]