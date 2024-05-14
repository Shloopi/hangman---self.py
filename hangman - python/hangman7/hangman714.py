def squared_numbers(start, stop):
    list = []
    while (start <= stop): # while start is less than or equal to stop
        list.append(start ** 2) # append the square of start to the list
        start += 1
        
    return list


print(squared_numbers(4, 8))