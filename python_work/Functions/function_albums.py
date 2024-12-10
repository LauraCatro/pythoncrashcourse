def make_album(artist_name, album_title, number_of_songs=None):
    album = {'Artist Name': artist_name, 'Album Title': album_title}
    if number_of_songs:
        album['Number of songs'] = number_of_songs
    return album


active = True
while active:
    print("\nPlese enter the information abount the album")
    print("enter 'q' when you finish")

    name = input("Artist Name: ")
    if name == 'q':
        break
    album = input("Album Name: ")
    if album == 'q':
        break
    songs = input("Number of songs: ")
    if songs == 'q':
        break

    album_information = make_album(name, album, songs)
    print(album_information)

# Dictionary
# album_information = make_album('Ariana Grande', 'Thank u next')
# print(f"\n{album_information}")

# album_information = make_album('BTS', '7')
# print(f"\n{album_information}")

# album_information = make_album('Rauw Alejandro', 'Desenfocao')
# print(f"\n{album_information}")

# Including the number of songs
# album_information = make_album('Ariana Grande', 'Thank u next', 12)
# print(f"\n{album_information}")
