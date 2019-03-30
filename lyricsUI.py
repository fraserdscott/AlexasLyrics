import pylyrics3
import random
import tkinter
from tkinter import *

songs = [('Smash Mouth','All Star'),
         ('Oasis','Wonderwall'),
         ('John Lennon','Imagine'),
         ('Eminem','Lose Yourself')]

    
def getRandomSong():
    # Pick a random song
    song = random.choice(songs)
    artist = song[0]
    title = song[1]

    # Retrieve lyrics from lyrics wiki and split into list
    string = pylyrics3.get_song_lyrics(artist, title)
    lyrics = str.splitlines(string)

    return artist, title, lyrics


def lyricsUI():
    
    class Application(Frame):

        def __init__(self, master=None):
            super().__init__(master)
            self.master = master
            self.pack()
            self.create_widgets()

            #while True:
            self.newSong()
            
        def create_widgets(self):
                        
            top = Frame(root)
            bottom = Frame(root)
            top.pack(side=TOP)
            bottom.pack(fill=BOTH, expand=True)
            
            self.title = Label(self, text="Lyrics Puzzler", fg="blue", font=("Helvetica", 16))
            self.title.pack(side = TOP)
                        
            self.listbox = Listbox(self, width=100)
            self.listbox.pack(fill=X, expand=1)

            self.entry = Entry(bottom, width=80)
            self.entry.pack(side = LEFT)

            self.lyricButton = Button(bottom, width=20, text = "Guess", command = self.makeGuess)
            self.lyricButton.pack(side = RIGHT)

            root.bind('<Return>', self.pressEnter)


        def pressEnter(self,event):
            self.makeGuess()

            
        def makeGuess(self):
            
            if self.entry.get().lower() == self.title.lower():
                self.newSong()
                return
            
            self.i += 1
            self.listbox.insert(END, self.lyrics[self.i])
            
        
        def newSong(self):
            self.listbox.delete(0,END)
            self.entry.delete(0,END)
            
            self.artist, self.title, self.lyrics = getRandomSong() 

            self.i = 0

            self.listbox.insert(END, self.lyrics[self.i])
            
            
    root = Tk()
    app = Application(master=root)
    app.mainloop()