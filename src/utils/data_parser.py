from src.models.Song import Song
from src.models.Artist import Artist
from src.models.Album import Album

def tracks_to_songs(tracks):
  songs = []

  for track in tracks["items"]:
    album = Album(track["album"])
    artists = []
    for artist in track["artists"]:
      artists.append(Artist(artist))

    song = Song(track)
    song.set_album(album)
    song.set_artists(artists)
    songs.append(dict(song))
  
  return songs
