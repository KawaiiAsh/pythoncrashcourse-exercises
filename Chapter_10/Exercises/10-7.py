def print_file(filename):
    try:
        with open(filename,'r') as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print(filename.title() + " not found!")
    else:
        print(contents.rstrip())

filenames = ['cats.txt','dogs.txt']
for filename in filenames:
    print_file(filename)        