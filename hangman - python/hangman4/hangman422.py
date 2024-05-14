msg = input("Enter a message: ")
msg = msg.replace(" ", "") # Remove spaces
msg = msg.lower() # Convert to lowercase

if msg == msg[::-1]: # Compare the original message with its reverse
    print("OK")
else: # If the message is not a palindrome
    print("NOT")