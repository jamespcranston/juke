from spotify import Playlist

class PlaylistWrapper(Playlist):
	def __init__(self, name, creator):
		super().__init__()
		self.ranking_map = defaultdict(int)
		self.name = name
		self.creator = spotify.remembered_user_name

	# call this whenever any upvote/downvote is pressed or song is queued to preserve order
	def sort_tracks(self):
		self.tracks = sorted(self.tracks, key = lambda track: ranking_map[track])

	# note that tracks can be single track or list of tracks
	def add_tracks(self, tracks, index = None):
		super().add_tracks(tracks, index)
		# if a track is being queued for the first time, net_vote == 1
		# if track already in queue, increment net_vote
		for track in tracks:
			ranking_map[track] += 1
		self.sort_tracks()

	# note that indexes can be single index or list of indexes
	# call this with indexes = 0 whenever song front of queue is finished playing or skip button is pressed
	def remove_tracks(indexes):
		if isinstance(indexes, int):
			indexes = [indexes]

		try:
			tracks_to_remove = [self.tracks[i] for i in indexes]
		except IndexError:
			pass

		for track in tracks_to_remove:
			ranking_map.remove(track) 

		super().remove_tracks(indexes)




