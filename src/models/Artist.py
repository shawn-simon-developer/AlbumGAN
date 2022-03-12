class Artist:
  def __init__(self, apiArtist):
    self.id = apiArtist["id"]
    self.name = apiArtist["name"]
