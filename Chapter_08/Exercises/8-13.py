def build_profile(first,last,**user_info):
    user_profile = {}
    user_profile['first'] = first
    user_profile['last'] = last
    for key,value in user_info.items():
        user_profile[key] = value
    return user_profile

my_profile = build_profile('Ash','Kawaii',hobby='Coding',gender='male',age=21)
print(my_profile)
