# new game menu
#
import tkinter as tk
from random import shuffle
from PIL import ImageTk, Image
from getCards import getNum


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
        for F in (MainMenu, gamePage, showGame):

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

        #Deal Button
        self.dealbutt = tk.Button(self.canvas, text="Deal", font=("Verdana", 12), command=lambda: dealCards(controller))
        self.dealbutt.place(x=320, y=500)

        #initialize bets total
        self.bet_total = 0
        self.balance = 1000

        #Bet Buttons
        self.bet1 = tk.Button(self.canvas,text="$1", width=3, height=1, command = lambda: addBet(self,1))
        self.bet1.place(x=30, y=500)
        self.bet5 = tk.Button(self.canvas,text="$5",width=3, height=1, command = lambda:addBet(self,5))
        self.bet5.place(x=65, y=500)
        self.bet25 = tk.Button(self.canvas,text="$25",width=3, height=1, command = lambda:addBet(self,25))
        self.bet25.place(x=100, y=500)
        self.bet100 = tk.Button(self.canvas,text="$100",width=3, height=1, command = lambda:addBet(self,100))
        self.bet100.place(x=135, y=500)

        #Balance label
        balancetext = self.canvas.create_text(550, 500, anchor="nw")
        self.canvas.itemconfig(balancetext, text="Balance: " + str(self.balance), font=("Verdana", 12), fill="white")

        #Bet amount label
        bettext = self.canvas.create_text(317, 450, anchor="nw")
        self.canvas.itemconfig(bettext, text="Bet: " +str(self.bet_total), font=("Verdana", 12), fill="white")

        #Summing total bets
        def addBet(self, amt):
            self.bet_total = self.bet_total + amt
            self.balance = self.balance - amt

            #Print updated balance
            self.canvas.itemconfig(balancetext, text="Balance: " + str(self.balance), font=("Verdana", 12), fill="white")
            self.canvas.itemconfig(bettext, text="Bet: " +str(self.bet_total), font=("Verdana", 12), fill="white")

        #dealCards function randomly shuffles a deck of cards
        #and returns 14 cards (14 cards allows for up to 7
        #cards being dealt to both the dealer and player)
        def dealCards(controller):
            deckrange = list(range(0,52))

            def Shuffle():
                deckorder = shuffle(deckrange)
                return deckorder

            def pullCards(amt):
                deckorder = Shuffle()
                cardskey = []
                for i in range(amt):
                    cardskey.append(deckrange.pop())

                return cardskey

            global cards
            cards = pullCards(14) #pulls 14 cards in order of shuffle

            #Remove Deal button when pressed
            self.dealbutt.destroy()

            #Disable bet Buttons
            self.bet1.configure(state="disabled")
            self.bet5.configure(state="disabled")
            self.bet25.configure(state="disabled")
            self.bet100.configure(state="disabled")

            #Hit and Stand Buttons
            self.hitbutt = tk.Button(self.canvas, text="Hit", width=7, height=2, command = lambda: hitCard())
            self.hitbutt.place(x=290, y=500)
            self.standbutt = tk.Button(self.canvas, text="Stand", width=7, height=2, command = lambda: standCard())
            self.standbutt.place(x=350, y=500)

            #Display Cards
            card_img = Image.open("Images\\PlayingCard.png")
            self.cardimg = ImageTk.PhotoImage(card_img.resize((100,150), Image.ANTIALIAS))
            self.bg = self.canvas.create_image(200,200, anchor=tk.NW, image=self.cardimg)

            #PLAYER CARD 1
            x = getNum()
            print(x)


            #DEALER CARD 1


            #PLAYER CARD 2


            #DEALER CARD 2

class showGame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #bg canvas img
        self.canvas = tk.Canvas(self, width=700, height=600)
        self.canvas.pack()

        pil_img = Image.open("Images\\blackjack_background.jpg")
        self.img = ImageTk.PhotoImage(pil_img.resize((700, 600), Image.ANTIALIAS))
        self.bg = self.canvas.create_image(0,0, anchor=tk.NW, image=self.img)





        #USE FOR TEXT SOMEWHERE
        #dealtext = self.canvas.create_text(270, 500, anchor="nw")
        #self.canvas.itemconfig(dealtext, text="Deal", font=("Verdana", 12), fill="white")


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
