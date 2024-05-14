msg = input("Enter a message: ")

print(msg[0] + msg[1:].replace(msg[0], "e"))