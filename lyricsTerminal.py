import pylyrics3
import random
from my_lyrics import get_popular_song


def getRandomSong():
    # Pick a random song
    song = random.choice(songs)
    artist = song[0]
    title = song[1]

    # Retrieve lyrics from lyrics wiki and split into list
    string = pylyrics3.get_song_lyrics(artist, title)
    lyrics = str.splitlines(string)

    return artist, title, lyrics


def lyricsTerminal():

    # Lyric guessing game to run on python terminal
    
    while True:

        lyrics, artist, title = get_popular_song()

        print("____Lyrics Puzzler____")
        # Cycle through lines in song
        for i in range(len(lyrics)):

            print("\n  " + lyrics[i] + "\n")
            answer = input("Guess the song --> ")

            # If their answer is correct, stop giving lyrics
            if answer.lower() == title.lower():
                break
            print("Incorrect! Next lyric:")

        print("\nWell done! The song was " + title + " by " + artist + ".")
        print("You only needed " + str(i+1) + " lines of the song to guess correctly!\n\n")

lyricsTerminal()