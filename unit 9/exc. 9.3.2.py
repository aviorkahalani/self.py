# exc. 9.3.2
def my_mp4_playlist(file_path, new_song):
	songs_text = open(file_path, 'r')
	songs_data = songs_text.read()
	songs_data = songs_data.replace('Instrumental', new_song)
	songs_text.close()

	songs_text = open(file_path, 'w')
	songs_text.write(songs_data)
	songs_text.close()

	songs_text = open(file_path, 'r')
	for line in songs_text:
		print(line, end="")
	songs_text.close()





def main():
	file_path = r'C:\Users\כהלני\Desktop\self.py\unit 9\songs.txt'
	new_song = 'Python Love Story'
	my_mp4_playlist(file_path, new_song)


if __name__ == '__main__':
	main()