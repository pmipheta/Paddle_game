from bs4  import BeautifulSoup
import requests
from ytmusicapi import YTMusic
date = input("which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

url = f"https://appbrewery.github.io/bakeboard-hot-100/{date}"

response = requests.get(url)
song_page = response.text
soup = BeautifulSoup(song_page,"html.parser")

song_names = []
all_song_tag = soup.find_all(name="h3" , class_="chart-entry__title")

for tag in all_song_tag:
    song_name = tag.getText()
    song_name = song_name.strip()
    song_names.append(song_name)
print(song_names)

# YouTube Music Authentication
yt = YTMusic(r"c:\game\musical_game\browser.json")

# Create playlist
Player_Name = f"{date} Bill Board 100"
playlist_id = None
playlists = yt.get_library_playlists()

for i in playlists:
    if i["title"] == Player_Name:
        playlist_id = i["playlistId"]
        break
if playlist_id:
    print("already exist")
else:
    playlist_id = yt.create_playlist(
        title= Player_Name,
        description=f"Playlist with the hottest songs from {date}",
        privacy_status="PRIVATE",
    )
    print(f"Created playlist: {Player_Name}")

# Search and add each song

for song in song_names:
    try:
        searchs = yt.search(song,filter="songs")
        video = searchs[0]["videoId"]
        yt.add_playlist_items(playlist_id,[video])
        print(f"Added : {song}")

    except Exception as e:
        print(f"Cannot add {song}")
        print(e)