# exc. 9.3.1
def my_mp3_playlist(file_path):
	BIG_LIST = []
	songs_list = []
	songs_text = open(file_path, 'r')
	songs_data = [line.split(';') for line in songs_text.readlines()]
	# find the longest song:
	length_of_songs = []
	for longer in range(0, len(songs_data)):
		length = songs_data[longer][2]
		length = length.replace(":", "")
		length_of_songs.append(length)
	longest = max(length_of_songs)
	index = length_of_songs.index(longest)
	#print('The longest song is: ', songs_data[index][0])
	BIG_LIST.append(songs_data[index][0])
	# number of songs:
	number = len(songs_data)
	#print('Number of songs: ', number)
	BIG_LIST.append(number)
	# find the most frequent:
	count_list = []
	for band in range(0, len(songs_data)):
		name_of_band = songs_data[band][1]
		count_list.append(name_of_band)
	counter = 0
	num = count_list[0]

	for y in count_list:
		curr_frequency = count_list.count(y)
		if curr_frequency > counter:
			counter = curr_frequency
			num = y
	#print('The most frequent band is: ', num)
	BIG_LIST.append(num)
	print(tuple(BIG_LIST))
	songs_text.close()


def main():
	file_path = r'C:\Users\כהלני\Desktop\self.py\unit 9\songs.txt'
	my_mp3_playlist(file_path)


if __name__ == '__main__':
	main()