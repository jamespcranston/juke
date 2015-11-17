import spotify
import searcher


global session
global playlist_container
global curr_playlist
global audio_sink

def show_playlists():
	for index, playlist in enumerate(playlist_container):
		playlist = playlist.load()
		print('Index: {} Name: {} Number of Tracks: {}'.format(index, playlist.name, len(playlist.tracks)))
	index = int(input('*** choose index of playlist to join: '))
	curr_playlist = playlist_container[index]
	print('Successfully joined {}!'.format(curr_playlist.name))

def show_songs_on_playlist():
	for index, track  in enumerate(curr_playlist.tracks):
		print('Index: {} Track: {}  Artist: {} Popularity: {}\n'.format(index, track.name, track.artists[0].load().name,
		 	track.popularity))

def play_song(track):
	session.player.load(track)
	session.player.play()

def add_song():
	track_name = input('*** track to search for: ')
	search = searcher.Searcher(session)
	results = search.find_track_list(track_name, session)
	for index, entry in enumerate(results):
		print('Index: {} Track: {}  Artist: {} Popularity: {}\n'.format(index, entry['track'].name, entry['artist'],
		 entry['popularity']))
	index = int(input('*** choose index of song to add: '))
	curr_playlist.add_tracks(results[index]['track'])
	print('{} successfully added to {}!'.format(results[index]['track'].name, curr_playlist.name))

def handle_playlist_action():
	while True:
		choice = input('*** (a)dd a song, (p)lay a song, (v)iew all playlists, (b)ack \n*** ').lower()[0]
		if choice == 'a':
			add_song()
		elif choice == 'p':
			show_songs_on_playlist()
			index = int(input('*** choose index of song to play: '))
			play_song(curr_playlist.tracks[index])
			stop = input("*** hit 's' to pause song playing \n").lower()[0]
			if stop == 's':
				session.player.pause()
		elif choice == 'v':
			show_playlists()
		elif choice == 'q':
			break

def create_playlist():
	name = input('playlist name: ')
	playlist_container.add_new_playlist(name, 0)
	global curr_playlist
	curr_playlist = playlist_container[0]

	handle_playlist_action()
	
def join_playlist(index):
	pass

def show_nearby_playlists():
	pass

def handle_main_menu():
	action = input('*** (c)reate a playlist or (q)uit? ').lower()[0]
	'''
	if action == 'v':
		show_nearby_playlists()
		playlist_index = input('*** enter the index of playlist you want to join: ')
		join_playlist(playlist_index)
	'''
	if action == 'c':
		create_playlist()

def login():
	user = input('*** spotify username: ')
	password = input('*** spotify password: ')
	session.login(user, password)
	while session.connection.state != spotify.ConnectionState.LOGGED_IN:
		session.process_events()
	print('Login successful!')

if __name__ == '__main__':
	print('*** Welcome to Juke! ***')
	session = spotify.Session()
	login()
	playlist_container = session.playlist_container.load()
	for index, playlist in enumerate(playlist_container):
		playlist_container.remove_playlist(index)
	audio_sink = spotify.PortAudioSink(session)
	handle_main_menu()





