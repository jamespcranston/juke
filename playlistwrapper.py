from spotify import Playlist
import TrackWrapper

class PlaylistWrapper(Playlist):
	def __init__(self):
		super().__init__()

	# call this whenever 
	def sort_tracks(self):
		self.tracks = sorted(self.tracks, key = lambda track: track.net_vote)

