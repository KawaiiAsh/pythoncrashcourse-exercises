def print_file(filename):
    try:
        with open(filename,'r') as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass
    else:
        print(contents.rstrip())

filenames = ['cats.txt','dogs.txt']
for filename in filenames:
    print_file(filename)        