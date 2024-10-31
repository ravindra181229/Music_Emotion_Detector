import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.getenv("SPOTIPY_CLIENT_ID"),
                                               client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
                                               redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
                                               scope="playlist-modify-public"))

# Function to create a playlist based on a mood
def create_mood_music(mood):

  my_spotify_user_id = sp.me()['id']

  playlist_name = f"{mood.capitalize()} Vibes"
  print(playlist_name)

  playlist_description = f"A playlist that matched Ravindra's {mood} mood."
  print(playlist_description)

  playlist = sp.user_playlist_create(
    user=my_spotify_user_id,
    name=playlist_name,
    description=playlist_description,
    public=True
  )

  print(f"created playlist: {playlist_name}")

  playlist_url = playlist['external_urls']['spotify']
  print("playlist url :",playlist_url)

  search_query = f"mood {mood}"
  search_result = sp.search(q=search_query,type='track',limit=10)

  tracks_uri = []
  for track in search_result['tracks']['items']:
    tracks_uri.append(track['uri'])

  sp.playlist_add_items(playlist_id=playlist['id'],items=tracks_uri)
  print(f"Added tracks to {playlist_name}")


mood = "excited"
create_mood_music(mood)



