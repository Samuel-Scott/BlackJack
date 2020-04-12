# new game menu
#

from tkinter import *

from random import shuffle

class Game(Tk):

    #Initialize frames for UI
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.geometry("800x700") # set window size


gametest = Game()
gametest.mainloop()
