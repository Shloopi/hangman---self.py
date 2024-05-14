import calendar

date_str = input("Enter a date (dd/mm/yyyy): ")

weekday_index = calendar.weekday(int(date_str[-4:]), int(date_str[3:5]), int(date_str[:2])) # get the weekday index from the date.

weekday = calendar.day_name[weekday_index] # get the weekday name from the index.

print(weekday)