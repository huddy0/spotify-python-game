from dotenv import load_dotenv
import os
import base64
from requests import post
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Authorization using .env variables. Spotify API key must be added to .env file.
 
load_dotenv()

client_id = os.getenv("dbc6f743e2ce4a1d93c7a2b00d0f6837")
client_secret = os.getenv("a6df35cdef845d2b18876b5bf7362b2")

# Authentication

# print(client_id)
# print(client_secret)

client_credentials_manager = SpotifyClientCredentials(client_id="dbc6f743e2ce4a1d93c7a2b00d0f6837", client_secret="fa6df35cdef845d2b18876b5bf7362b2")
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbNG2KDcFcKOF?si=1333723a6eff4b7f" # Playlist of choice
playlist_URI = playlist_link.split("/")[-1].split("?")[0]
track_name = [x["track"]["name"] for x in sp.playlist_tracks(playlist_URI)["items"]]
track_uris = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]

input = input()
result = sp.search(input)

for idx, track in enumerate(result['tracks']['items']):
    print(idx, track['name'])


# # Goes through playlist and prints name along with danceability score
# for track in sp.playlist_tracks(playlist_URI)["items"]:
#     name = track["track"]["name"]
#     energy = sp.audio_features(track["track"]["uri"])[0]["danceability"]
#     popularity = track["track"]["popularity"]

#     print(f"{name}  -  {energy}  -  {popularity}")




