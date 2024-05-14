def filter_teens(a, b, c):
   return fixed_age(a) + fixed_age(b) + fixed_age(c)

def fixed_age(age):
    fixed_age = age
    
    if age >= 13 and age <= 14 or age >= 17 and age <= 19: # if age is between 13 and 19 but not 15 or 16.
        fixed_age = 0
    
    return fixed_age


print(filter_teens(1, 2, 3)) # 6
print(filter_teens(2, 13, 1)) # 3
print(filter_teens(2, 15, 14)) # 17