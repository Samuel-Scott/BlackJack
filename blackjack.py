# new game menu
#
from tkinter import *
from random import shuffle
from PIL import ImageTk, Image

title_font = ("Verdana", 16)


class Game(Frame):

    #Initialize frames for UI
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

        # set background image
        image1 = ImageTk.PhotoImage(Image.open("Images\\blackjack_background.jpg"))
        imglabel = Label(self, image=image1)
        imglabel.image1=image1
        imglabel.place(x=0, y=0, relwidth=1, relheight=1)

        # set blackjack title
        l1 = Label(self, text="Online Blackjack", font=title_font)
        l1.place(x=250, y=100)

        Play_butt = Button(self, text="Login", command=lambda: print("test"))
        Play_butt.place(x=250, y=300)

        Exit_butt = Button(self, text="Exit", command=lambda: print("exit"))
        Exit_butt.place(x=250,y=350)

    def initUI(self):
      self.parent.title("BlackJack")
      self.pack(fill=BOTH, expand=1)

    def Play():
        print("test")

    def Exit():
        print("Exiting")
        exit()




root = Tk()
Game(root)
root.geometry("700x600")

root.mainloop()
