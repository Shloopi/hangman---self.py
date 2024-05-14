bricks_collected = int(input("Enter the number of bricks the pigs have collected (three digit number): ")) 
sum_bricks = bricks_collected % 10 + bricks_collected // 100 + (bricks_collected // 10) % 10 # sum of the digits of the number
print(sum_bricks)
print(sum_bricks // 3)
print(sum_bricks % 3)
print(sum_bricks % 3 == 0)