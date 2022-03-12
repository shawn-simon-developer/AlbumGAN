import asyncio
from src.modules import spotify
from src.utils import data_parser, file

async def main():
  token = await spotify.authenticate()
  tracks = await spotify.get_tracks(token)
  songs = data_parser.tracks_to_songs(tracks)

  print(f"{len(songs)} songs retrieved from spotify")

  file.write_to_csv('src/data/songs.csv', songs)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
