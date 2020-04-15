# new game menu
#
import tkinter as tk
from random import shuffle
from PIL import ImageTk, Image

title_font = ("Verdana", 16)


class Game(tk.Tk):

    #Initialize frames for UI
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.grid()
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # create frames
        for F in (MainMenu, gamePage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainMenu)

    # raise frame function
    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        ###


class MainMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # set canvas for bg img and labels
        self.canvas = tk.Canvas(self, width=700, height=600)
        self.canvas.pack()

        pil_img = Image.open("Images\\blackjack_background.jpg")
        self.img = ImageTk.PhotoImage(pil_img.resize((700, 600), Image.ANTIALIAS))
        self.bg = self.canvas.create_image(0,0, anchor=tk.NW, image=self.img)

        # set blackjack title
        #self.l1 = tk.Label(self.canvas, text="Online Blackjack", font=title_font)
        canvastext1 = self.canvas.create_text(240, 100, anchor="nw")
        self.canvas.itemconfig(canvastext1, text="Online Blackjack", font=("Verdana", 20), fill="white")
        #self.l1.place(x=250, y=100)

        self.Play_butt = tk.Button(self.canvas, width=10, height=1,
                                text="Play", font=("Verdana", 12),
                                command= lambda: controller.show_frame(gamePage))
        self.Play_butt.place(x=290, y=300)

        self.Exit_butt = tk.Button(self.canvas, width=10,
                                height=1, text="Exit", font=("Verdana", 12),
                                command= lambda: exit())
        self.Exit_butt.place(x=290,y=350)


class gamePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        #bg canvas img
        self.canvas = tk.Canvas(self, width=700, height=600)
        self.canvas.pack()

        pil_img = Image.open("Images\\blackjack_background.jpg")
        self.img = ImageTk.PhotoImage(pil_img.resize((700, 600), Image.ANTIALIAS))
        self.bg = self.canvas.create_image(0,0, anchor=tk.NW, image=self.img)

        #Text Labels


        dealtext = self.canvas.create_text(270, 500, anchor="nw")
        self.canvas.itemconfig(dealtext, text="Deal", font=("Verdana", 12), fill="white")







class Login(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        print("test login")



class gameExit(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        exit()

root = Game()
root.geometry("700x600")
root.resizable(width=False, height=False)
root.wm_attributes("-transparentcolor", 'grey')
root.mainloop()
