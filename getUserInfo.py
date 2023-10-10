import spotipy
from spotipy.oauth2 import SpotifyOAuth

scopes = ["user-library-read", "user-top-read"]
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="4f57bdd6990d43bba5b4b45c4d7c1589",
                                               client_secret="45749f9145934ef39fe3c69e9e7fdc63",
                                               redirect_uri="http://127.0.0.1:9090",
                                               scope=scopes))
top_genres = {}
count = 1
print("Users Top 5 Songs")
results = sp.current_user_top_tracks(time_range='short_term', limit=6)
for item in results['items']:
    if item['name'] == "RAGE 2":
        continue
    print(count, item['name'], '-', item['artists'][0]['name'])
    count += 1
print()
count = 1
print("Users Top 5 Artists")
results = sp.current_user_top_artists(time_range='short_term', limit=5)
for item in results['items']:
    print(count, item['name'])
    count += 1
print()
count = 1
print("Users Top 5 Genres")
results = sp.current_user_top_artists(time_range='short_term', limit=40)
for item in results['items']:
    if len(item['genres']) == 0:
        continue
    if item['genres'][0] not in top_genres:
        top_genres[item['genres'][0]] = 1
        count += 1
    else:
        top_genres[item['genres'][0]] += 1

sorted_genres = dict(sorted(top_genres.items(), key=lambda item: item[1], reverse=True))
top_5_genres = list(sorted_genres.items())[:5]
count = 1
for genre in top_5_genres:
    print(count, genre[0])
    count += 1
