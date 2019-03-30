import pylyrics3
import random
from tkinter import *
from my_lyrics import get_popular_song


class Application(Frame):

    def __init__(self, master=None):
            super().__init__(master)
            self.master = master
            self.pack()
            self.create_widgets()

            self.newSong()
            
    # Create the UI elements: buttons, lists etc.
    def create_widgets(self):

        self.title = Label(self, text="Lyrics Puzzler", fg="blue", font=("Helvetica", 16))
        self.title.pack(side = TOP)

        self.lyricsBox = Listbox(self, width=100)
        self.lyricsBox.pack(fill=X, expand=1)

        # Create frame to store input field and button side by side
        bottom = Frame(root)
        bottom.pack(fill=BOTH, expand=True)
            
        self.entry = Entry(bottom, width=80)
        self.entry.pack(side = LEFT)

        self.lyricButton = Button(bottom, width=20, text = "Guess", command = self.makeGuess)
        self.lyricButton.pack(side = RIGHT)
        
        self.speak_button = Button(bottom, width=20, text="Speak", command = self.speak_lyric)
        self.speak_button.pack(side = RIGHT)

        # Bind enter button to make a guess
        root.bind('<Return>', self.pressEnter)
        
    
    def speak_lyric(self):
        pass
        

    # Handles pressing enter key instead of pressing button every time
    def pressEnter(self,event):
        self.makeGuess()

    # Handles checking if the users guess is right or wrong
    def makeGuess(self):
        
        # If the user has guessed right then give them a new song to guess
        if self.entry.get().lower() == self.title.lower():
            self.newSong()
            return

        # Otherwise the user has guessed wrong 
        self.lineNumber += 1
        if self.lineNumber==len(self.lyrics):
            self.newSong()
            
        self.lyricsBox.insert(END, self.lyrics[self.lineNumber]) # Show user next line of the song
        self.entry.delete(0, END) # Clear text input field
    
    # Reset UI and get a new song
    def newSong(self):
        # Clear the UI
        self.lyricsBox.delete(0,END)
        self.entry.delete(0,END)
        
        # Get a new song
        self.lyrics, self.artist, self.title = get_popular_song()
        print(self.title)
        self.lineNumber = 0

        self.lyricsBox.insert(END, self.lyrics[self.lineNumber])
            
            
root = Tk()
app = Application(master=root)
root.mainloop()
root.destroy()