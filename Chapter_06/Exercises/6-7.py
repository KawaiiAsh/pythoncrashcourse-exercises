friend1 = {'first_name':'ZhuangShui',
            'last_name':'Jiang',
            'age':21,
            'city':'NewYork'}
friend2 = {'first_name':'Yin',
           'last_name':'Lin',
           'age':22,
           'city':'LOS'}
friend3 = {'first_name':'Er',
           'last_name':'Jiu',
           'age':27,
           'city':'Chengdu'}
people = [friend1,friend2,friend3]
for friend in people:
    print("Friend's full name is: " + friend['last_name'] + friend['first_name'] +
          "He is " + str(friend['age']) + " years old. live in " + friend['city'])