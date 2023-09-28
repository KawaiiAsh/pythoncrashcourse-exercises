users = {
    'aeinstein': {
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
    },
    'mcurie':{
        'first':'marie',
        'last':'cure',
        'location':'paris',
    }
}

for username,user_info, in users.items():
    print("Username: " + username)
    full_name = user_info['last'] + " " + user_info['first']
    location = user_info['location']
    
    print("Fullname: " + full_name.title())
    print("Location: " + location.title())
