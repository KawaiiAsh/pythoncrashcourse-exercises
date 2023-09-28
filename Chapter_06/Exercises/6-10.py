cities = {
    'cheng du':{
        'country':'china',
        'population':10000000,
        'fact':'Chengdu is the capital city of the Chinese province of Sichuan.'
    },
    'new york':{
        'country':'united state',
        'population':66856889,
        'fact':'New York, often called New York City or NYC, is the most populous city in the United States.'
    }
}

for city,details in cities.items():
    print(city.title())
    country = details['country']
    population = details['population']
    fact = details['fact']

    print(f"{city.title()} is a part of {country} which has a population of {population} people. The information about this city is: {fact}\n")
