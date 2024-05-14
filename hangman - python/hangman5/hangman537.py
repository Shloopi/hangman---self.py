def chocolate_maker(small, big, x):
    BIG_BAR = 5
    
    return (small >= x % BIG_BAR) and (big >= x // BIG_BAR)


print(chocolate_maker(3, 1, 8))
print(chocolate_maker(3, 1, 9))
print(chocolate_maker(3, 2, 10))
