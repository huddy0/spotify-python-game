from dotenv import load_dotenv
import os
import base64
from requests import post
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

#Authentication - without user
client_credentials_manager = SpotifyClientCredentials(client_id="CLIENT_ID", client_secret="CLIENT_SECRET")
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbNG2KDcFcKOF?si=1333723a6eff4b7f"
playlist_URI = playlist_link.split("/")[-1].split("?")[0]
track_name = [x["track"]["name"] for x in sp.playlist_tracks(playlist_URI)["items"]]

for track in sp.playlist_tracks(playlist_URI)["items"]:
    print(track["track"]["name"])


