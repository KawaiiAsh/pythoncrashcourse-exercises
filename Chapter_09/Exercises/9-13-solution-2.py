from collections import OrderedDict

data = {
    'C':'Top 1 programming language',
    'Python':'Top 2 programming language',
    'React': 'Javascript library',
    'Django': 'Web framework',
    'Print()': 'A function',
    'Set()': 'A function',
    'For': 'Forloop',
    'While': 'Whileloop'
}

dict = OrderedDict(data)

for name,meaning in data.items():
    print(name.title() + " is " + meaning.title() + ".")
