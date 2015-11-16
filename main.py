import spotify

global session

def create_playlist():
	name = input('playlist name: ')
	track_name = input('track to search for: ')
	search = session.search(track_name)
	search.load()
	print(search.tracks)

def join_playlist(index):
	pass

def show_nearby_playlists():
	pass

def handle_main_menu():
	action = input('(v)iew nearby playlists, (c)reate a playlist, or (q)uit? ').lower()[0]
	if action == 'v':
		show_nearby_playlists()
		playlist_index = input('enter the index of playlist you want to join: ')
		join_playlist(playlist_index)
	elif action == 'c':
		create_playlist()

def login():
	user = input('spotify username: ')
	password = input('spotify password: ')
	session.login(user, password)
	while session.connection.state != spotify.ConnectionState.LOGGED_IN:
		session.process_events()
	print('Login successful!')

if __name__ == '__main__':
	print('Welcome to Juke!')
	session = spotify.Session()
	login()
	handle_main_menu()





