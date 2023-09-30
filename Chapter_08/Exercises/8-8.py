def make_album(singer_name,album_name,song_number=""):
    album_info = {'singer name'.title():singer_name.title(),
                  'album name'.title():album_name.title()}
    if song_number:
        album_info['song number'.title()] = song_number
    return album_info

while True:
    message = "(Enter 'q' to end the program.)"
    print(message)
    singer_name = input("Please enter singer's name:")
    if singer_name == 'q':
        break
    album_name = input("Please enter album's name:")
    if album_name == 'q':
        break
    song_number = input("Please enter song_number(options):")
    if song_number == 'q':
        break
    if song_number.isdigit():
        song_number = int(song_number)
    album_info = make_album(singer_name,album_name,song_number)
    print(album_info)
