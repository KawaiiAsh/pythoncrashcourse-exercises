current_users = ['asheone18','kawaiiash','newplayer','forever18','gggonext']
new_users = ['asheone18','newbro','forever18','123456','okgg']

for new_user in new_users:
    if new_user in current_users:
        print(f"username {new_user} already use.")
    else:
        print(f"username {new_user} is fine!")