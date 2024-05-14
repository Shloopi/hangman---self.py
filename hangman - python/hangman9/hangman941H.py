def choose_word(file_path, index): 
    returned_word = ()
    
    with open(file_path, 'r') as file:
        # splits the file with spaces to get all of the words.
        words = file.read().split('\n')
        
        # turn the list into a hashset (dictionary) to remove duplicates.
        words = list(dict.fromkeys(words))
        
        # number of words in the list.
        num_of_words = len(words)
        
        # save a tuple with the number of words and the chosen word.
        returned_word = (num_of_words, words[((index - 1) % num_of_words)])
        
    return returned_word
    
        
# print(choose_word(r"C:\Users\idan2\Desktop\Hermlin\צבא\python\hangman9\words.txt", 3))
# print(choose_word(r"C:\Users\idan2\Desktop\Hermlin\צבא\python\hangman9\words.txt", 15))
