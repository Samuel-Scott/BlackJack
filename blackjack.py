# new game menu
#

from tkinter import *

from random import shuffle

class Game(Tk):

    #Initialize frames for UI
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        app = Tk()

        self.geometry("800x700") # set window size

        backpic = PhotoImage(file = "C:\\Images\\background.jpeg")
        label1 = Label(self, image=backpic).pack()


gametest = Game()
gametest.mainloop()
