import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Put Spotify api data here
SPOTI_CLIENT_ID = "7d9c8c83a0954453a0194a2882cbb249"
SPOTI_CLIENT_SECRET = "e6e9cf44764b487e9c4936fdae41d840"
SPOTI_REDIRECT_URI = "http://example.com"

user_input = input("Enter a date in the format YYYY-MM-DD: ")
url = f"https://www.billboard.com/charts/hot-100/{user_input}"

# Parsing the Billboard website
webpage = requests.get(url).text
soup = BeautifulSoup(webpage, "html.parser")

songs_artist = soup.select(selector="ul.o-chart-results-list-row li:last-child ul li:first-child h3")
songs_name = soup.select(selector="ul.o-chart-results-list-row li:last-child ul li:first-child span")

# Authorazing to the Spotify API through Spotipy lib
scope = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=SPOTI_CLIENT_ID, client_secret=SPOTI_CLIENT_SECRET, redirect_uri=SPOTI_REDIRECT_URI))

# Creating a Spotify playlist
result = sp.user_playlist_create(sp.me()['id'], f"Top 100 songs from {user_input}", public=False, collaborative=False, description='Top 100 songs from Billboard top 100 by the date')
playlist_id = result["id"]

# Gettings URIs of the tracks
top100_songs_URI = []

for (a, n) in zip(songs_artist, songs_name):
    result = sp.search(f"artist: {n.get_text().strip()} track: {a.get_text().strip()}", 1, 0, "track")
    try:
        top100_songs_URI.append(result["tracks"]["items"][0]["uri"])
    except IndexError:
        pass

# Adding tracks to the playlist
result = sp.playlist_add_items(playlist_id, top100_songs_URI, position=None)