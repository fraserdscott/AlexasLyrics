import pylyrics3
import csv
import random

# return a 2-d list 
# where each list element has a sublist where the 
# first element is the artist and the second the title of the song
def read_songs(filename):
    artist_song_title = []
    with open(filename, 'r', encoding='utf8') as my_read_file:
        reader = csv.reader(my_read_file)
        for i ,row in enumerate(reader):
            if i > 0:
                artist = str(row[2])
                song_title = str(row[3])
                artist_song_title.append([artist, song_title])
    
    return artist_song_title

# Returns a list of lyrics line by line
# the artist and the song too
def get_popular_song():
    artist_song = read_songs('chart2000-songyear-0-3-0048.csv')
    N = len(artist_song)
    rn = random.randint(0, N)
    artist, song = artist_song[rn]
    lyrics = pylyrics3.get_song_lyrics(artist, song)
    if lyrics is None:
        return get_popular_song()
    lyrics = lyrics.split('\n')
    formated_lyrics = []
    for lyric in lyrics:
        formated_lyrics.append(lyric.strip())

    return formated_lyrics, artist, song


l, a, s = get_popular_song()
print(l)



