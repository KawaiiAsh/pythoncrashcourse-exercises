def make_album(singer_name,album_name,song_number=""):
    album_info = {'singer name'.title():singer_name.title(),
                  'album name'.title():album_name.title()}
    if song_number:
        album_info['song number'.title()] = song_number
    return album_info

album_info = make_album("Jay",'Love Confession')
print(album_info)
album_info = make_album("Jay",'Love Confession',10)
print(album_info)