from collections import OrderedDict

dict = OrderedDict()

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

for name,meaning in data.items():
    dict[name] = meaning

for name,meaning in data.items():
    print(name.title() + " is " + meaning.title() + ".")
