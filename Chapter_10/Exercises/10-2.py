file_name = 'learning_python.txt'
text = ''

with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    text = line.replace('Python','C++')
    
print(text)