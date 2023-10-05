def count_word(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.") 

filenames = ['alice.txt','pi_digits.txt','pi_million_digits.txt']
for filename in filenames:
    count_word(filename)