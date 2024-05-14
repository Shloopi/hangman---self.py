msg = input("Enter a message: ")

print(msg[:len(msg) // 2].lower() + msg[len(msg) // 2:].upper())