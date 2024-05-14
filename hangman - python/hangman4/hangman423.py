temperature = input("Enter the temperature you want to convert: ")

is_celsius = temperature[-1] == "C" # check if the temperature is in Celsius

temperature = float(temperature[:-1]) # remove the last character and convert to integer

converted_temperature = 0.0

if is_celsius: # if the temperature is in Celsius
    converted_temperature = temperature * 9 / 5 + 32 # convert to Fahrenheit
else:
    converted_temperature = (temperature * 5 - 160) / 9 # convert to Celsius

if converted_temperature == int(converted_temperature):
    converted_temperature = int(converted_temperature)
    
print(str(converted_temperature) + ("F" if is_celsius else "C")) # print the converted temperature with the correct unit