import pylyrics3
import random
from tkinter import *
from my_lyrics import get_popular_song

def lyricsUI():
    
    class Application(Frame):

        def __init__(self, master=None):
            super().__init__(master)
            self.master = master
            self.pack()
            self.create_widgets()

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


        # Handles pressing enter key instead of pressing button every time
        def pressEnter(self,event):
            self.makeGuess()


        def makeGuess(self):
            
            if self.entry.get().lower() == self.title.lower():
                self.newSong()
                return
            
            self.i += 1
            self.listbox.insert(END, self.lyrics[self.i])
            self.entry.delete(0, END)
            
        # Reset UI and get a new song
        def newSong(self):
            self.listbox.delete(0,END)
            self.entry.delete(0,END)
            
            self.lyrics, self.artist, self.title = get_popular_song()
            print(self.title)

            self.i = 0

            self.listbox.insert(END, self.lyrics[self.i])
            
            
    root = Tk()
    app = Application(master=root)
    app.mainloop()
