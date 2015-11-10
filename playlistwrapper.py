from spotify import Playlist

class PlaylistWrapper(Playlist):
	def __init__(self):
		super().__init__()
		self.ranking_map = defaultdict(int)



	# call this whenever any upvote/downvote is pressed or song is queued to preserve order
	def sort_tracks(self):
		self.tracks = sorted(self.tracks, key = lambda track: ranking_map[track])

	def add_tracks(self, tracks):
		# if a track is being queued for the first time, net_vote == 1
		# if track already in queue, increment net_vote
		for track in tracks:
			ranking_map[track] += 1
		self.sort_tracks()

	




