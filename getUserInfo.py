import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
import sys

scopes = ["user-library-read", "user-top-read"]
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="4f57bdd6990d43bba5b4b45c4d7c1589",
                                               client_secret="45749f9145934ef39fe3c69e9e7fdc63",
                                               redirect_uri="http://127.0.0.1:9090",
                                               scope=scopes))
top_songs = []
top_artists = []
print("Users Top 5 Songs")
results = sp.current_user_top_tracks(time_range='short_term', limit=5)
for i, item in enumerate(results['items']):
    print(i+1, item['name'], '-', item['artists'][0]['name'])
    top_songs.append(item['name'])
print()
print("Users Top 5 Artists")
results = sp.current_user_top_artists(time_range='short_term', limit=5)
for i, item in enumerate(results['items']):
    top_artists.append(item['name'])
    print(i+1, item['name'])





