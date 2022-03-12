class Album:
  def __init__(self, apiAlbum):
    self.id = apiAlbum["id"]
    self.name = apiAlbum["name"]
    self.type = apiAlbum["type"]
    self.releaseDate = apiAlbum["release_date"]

  def set_artists(self, apiArtists):
    self.artists = apiArtists
