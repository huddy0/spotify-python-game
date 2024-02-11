from dotenv import load_dotenv
import os
from requests import post
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random
import pandas as pd

# Authorization using .env variables. Spotify API key must be added to .env file.
 
load_dotenv()

client_id = os.getenv("dbc6f743e2ce4a1d93c7a2b00d0f6837")
client_secret = os.getenv("a6df35cdef845d2b18876b5bf7362b2")

client_credentials_manager = SpotifyClientCredentials(client_id="dbc6f743e2ce4a1d93c7a2b00d0f6837", client_secret="fa6df35cdef845d2b18876b5bf7362b2")
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

# playlist_link = "https://open.spotify.com/playlist/0Hm1tCeFv45CJkNeIAtrfF?si=92aefe803da846cd" # Playlist of choice
# playlist_URI = playlist_link.split("/")[-1].split("?")[0]
# track_name = [x["track"]["name"] for x in sp.playlist_tracks(playlist_URI)["items"]]
# track_uris = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]

score = 0
artists = pd.read_csv("./artists.csv")

# Generates a random artist from the artist list
def searchRandomArtist(artist):
    randomArtist = random.choice(artists['artist'])
    result = sp.search(randomArtist, limit=1,type = 'artist', market="US")
    return result['artists']['items'][0]


print("\n Welcome to the Spotify Game \n")
print("Choose Who Is More Popular\n Type 1 for Left     Type 2 for Right\n")

while True:
    artist1 = searchRandomArtist(artists)
    artist2 = artist1
    while artist1 == artist2:
        artist2 = searchRandomArtist(artists)
    print(f"-------------------------------------------")
    print(f"  |{artist1['name']}|  v.s.  |{artist2['name']}|")
    print(f"-------------------------------------------")
    if artist1['popularity'] >= artist2['popularity']:
        correct = 1
    else:
        correct = 2
    answer = input()
    try:
        if int(answer) == correct:
            score += 1
            print(f"Current Score: {score}")
        else:
            print("Incorrect!")
            print(f"Final Score: {score}")
            break
    except:
        print("Invalid...\nExiting...")
        break