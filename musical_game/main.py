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
# print(song_names)
yt = YTMusic(r"c:\game\musical_game\browser.json")
playlists = yt.get_library_playlists()
print(f"Found {len(playlists)} playlists in your library.")

## will fix tommorow 
playlistId = YTMusic.create_playlist(
    "test",
    "test description"
)