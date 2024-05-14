def distance(num1, num2, num3):
    check_close = abs(num2 - num1) == 1 or abs(num3 - num1) == 1 # check if the difference between the numbers is 1
    check_far = abs(num2 - num1) >= 2 or abs(num3 - num1) >= 2 # check if the difference between the numbers is 2 or more
    return check_close and check_far


print(distance(1, 2, 10))

print(distance(4, 5, 3))
