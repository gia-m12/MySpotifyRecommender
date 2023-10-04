import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="4f57bdd6990d43bba5b4b45c4d7c1589",
                                               client_secret="45749f9145934ef39fe3c69e9e7fdc63",
                                               redirect_uri="http://localhost:8888/callback",
                                               scope="user-library-read"))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])
