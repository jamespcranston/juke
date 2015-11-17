
import spotify

class Searcher():
	def __init__(self, session):
		self.session = session

	# given a track name, this method should return a list containing a dictionary for 
	# top 10 search results. Format: 
	# [{'track': ~ ,artist': ~, album': ~ , 'duration': ~ , 'popularity': ~ }, etc.]
	# note that 'track' should map to an actual track object that will later be used by the audio player 
	# to load/play the track
	def find_track_list(self, track_name, session):
		tracks = session.search(track_name).load().tracks
		if len(tracks) is 0:
			return

		list_to_return = []
		for index in range(len(tracks)):
			if index > 9:
				break
			d = {}
			track = tracks[index].load()
			d['track'] = track
			d['artist'] = track.artists[0].load().name
			d['album'] = track.album.load().name
			d['popularity'] = track.popularity
			list_to_return.append(d)
		return list_to_return
