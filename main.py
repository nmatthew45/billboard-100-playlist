import requests
import spotipy
from bs4 import BeautifulSoup
from dotenv import dotenv_values
from spotipy import SpotifyOAuth

# Load environment variables
config = dotenv_values(".env")

# Ask user for date to make a request to billboard top 100
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

# Make a request and store into a response variable
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)

# Create a soup object
soup = BeautifulSoup(response.text, 'html.parser')

# Scrape the response and create a list of song names
div_container = soup.find_all("div", class_="o-chart-results-list-row-container")
song_names = [song.find("h3").getText().strip("\n") for song in div_container]

# Can also retrieve list of artist names
# artist_names = [artist.find("h3").find_next_sibling("span").getText().strip("\n") for artist in div_container]

# Create spotipy object that uses Authorization Code flow
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=config['CLIENT_ID'],
                                               client_secret=config['CLIENT_SECRET'],
                                               redirect_uri=config['REDIRECT_URI'],
                                               scope='playlist-modify-private',
                                               show_dialog=True,
                                               cache_path='token.txt'
                                               ))

user_id = sp.current_user()['id']
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song_names[song]} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist['id'], items=song_uris)
