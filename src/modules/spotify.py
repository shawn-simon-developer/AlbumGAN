import requests
import base64
from src.utils.file import read_file

TOKEN_URL = "https://accounts.spotify.com/api/token"
BASE_URL = "https://api.spotify.com/v1"

async def authenticate():
  config = read_file("src/config/spotify.json")
  response = requests.post(TOKEN_URL, data = config)

  res = response.json()

  if response.status_code == 200:
    return res["access_token"]
  else:
    raise Exception("Unable to authenticate", res)
    
# Search
async def search(
  token, 
  q = "",
  type = "track", 
  limit = 20, 
  offset = 0
):
  headers = { "Authorization": f"Bearer {token}"}
  url = f"{BASE_URL}/search"

  if (q == ""): url+="?q=''"

  payload = { 
    "q": q, 
    "type": type, 
    "limit": limit, 
    "offset": offset 
  }

  return requests.get(
    url,
    params=payload,
    headers=headers
  )

# Search for tracks
async def get_tracks(token, q=""):
  response = await search(token, type="track", q=q)
  res = response.json()

  if response.status_code == 200:
    return res["tracks"]
  else:
    raise Exception("Unable to get tracks", res)
    
# Search for artists
async def get_artists(token, q=""):
  response = await search(token, type="artist", q=q)
  res = response.json()

  if response.status_code == 200:
    return res["artists"]
  else:
    raise Exception("Unable to get artists", res)

# Search for albums
async def get_albums(token, q=""):
  response = await search(token, type="album", q=q)
  res = response.json()

  if response.status_code == 200:
    return res["albums"]
  else:
    raise Exception("Unable to get albums", res)
