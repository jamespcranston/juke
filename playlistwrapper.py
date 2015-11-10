from spotify import Playlist

class PlaylistWrapper(Playlist):
	def __init__(self):
		super().__init__()

	# call this whenever 
	def sort_tracks(self):
		for track in self.tracks:
			
