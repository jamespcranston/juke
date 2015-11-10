from spotify import Track

class TrackWrapper(Track):
	def __init__(self):
		super().__init__()
		self.net_vote = 0
		