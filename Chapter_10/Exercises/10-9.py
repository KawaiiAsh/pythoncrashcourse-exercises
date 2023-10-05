def count_word(filename):
    try:
        with open(filename,'r',encoding='UTF-8') as file_object:
            contents = file_object.read()
    except FileNotFoundError:
            print("File not found!")
    else:
        word_count = contents.lower().count('the')
        print("The number of 'the' is " + str(word_count) + ".")

count_word('gutenberg.txt')