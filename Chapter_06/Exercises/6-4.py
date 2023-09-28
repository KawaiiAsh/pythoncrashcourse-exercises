dict = {
    'C':'Top 1 programming language',
    'Python':'Top 2 programming language',
    'React': 'Javascript library',
    'Django': 'Web framework',
    'Print()': 'A function',
    'Set()': 'A function',
    'For': 'Forloop',
    'While': 'Whileloop'
}

for word,meaning in dict.items():
    print("Word: " + word.title() + ", Meaning: " + meaning.title())