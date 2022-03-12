class Song:
	def __init__(self, apiSong):
		self.id = apiSong["id"]
		self.name = apiSong["name"]
		self.popularity = apiSong["popularity"]

	# deep dict
	def __iter__(self):
		for key in self.__dict__:
			if (key == 'album'):
				yield key, getattr(self, key).__dict__
			elif (key == 'artists'):
				artists = []
				for a in getattr(self, key):
					artists.append(a.__dict__)
				yield key, artists
			else:
				yield key, getattr(self, key)

	def set_album(self, album):
		self.album = album

	def set_artists(self, artists):
		self.artists = artists
