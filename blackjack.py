# new game menu
#
import tkinter as tk
from random import *
from PIL import ImageTk, Image
from getCards import getCardPath, getValue

#------------------TO-DO LIST--------------------#
#Add bust functionality
#Add stand function
#dealer hit cards
#Gain money for winning
#

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
        self.dealbutt = tk.Button(self.canvas, text="Deal", font=("Verdana", 12), state="disabled", command=lambda: dealCards(controller))
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

            #Enable deal button if bet has been placed
            if self.bet_total > 0:
                self.dealbutt.config(state="normal")


        #dealCards function randomly shuffles a deck of cards
        #and returns 14 cards (14 cards allows for up to 7
        #cards being dealt to both the dealer and player)
        def dealCards(controller):
            deckrange = list(range(1,52))

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
            #for i in range(len(cards)):
            #    print(cards[i])

            #Remove Deal button when pressed
            self.dealbutt.destroy()

            #Disable bet Buttons
            self.bet1.configure(state="disabled")
            self.bet5.configure(state="disabled")
            self.bet25.configure(state="disabled")
            self.bet100.configure(state="disabled")

            #Hit and Stand Buttons, show once cards are dealt
            self.hitbutt = tk.Button(self.canvas, text="Hit", width=7, height=2, command = lambda: hitCard())
            self.hitbutt.after(2500, lambda: self.hitbutt.place(x=290, y=500))
            self.standbutt = tk.Button(self.canvas, text="Stand", width=7, height=2, command = lambda: standCard())
            self.standbutt.after(2500, lambda: self.standbutt.place(x=350, y=500))

            #------------------Cards Display and Counting---------------------#
            self.player_cardtot = 0
            self.dealer_cardtot = 0

            self.player_cards = {} #create dic to hold player card values

            #PLAYER CARD 1
            card_p1 = Image.open(getCardPath(cards[0]))
            self.cardimgp1 = ImageTk.PhotoImage(card_p1.resize((100,150), Image.ANTIALIAS))
            self.canvas.after(750, lambda: self.canvas.create_image(250,250, anchor=tk.NW, image=self.cardimgp1))
            self.player_cardtot += getValue(cards[0])
            self.player_cards[1] = getValue(cards[0])

            #DEALER CARD 1 (NO SHOW)
            card_d1 = Image.open("Images\\Cards\\gray_back.png")
            self.cardimgd1 = ImageTk.PhotoImage(card_d1.resize((100,150), Image.ANTIALIAS))
            self.canvas.after(1250, lambda: self.canvas.create_image(250,50, anchor=tk.NW, image=self.cardimgd1))
            self.dealer_cardtot += getValue(cards[1])

            #PLAYER CARD 2
            card_p2 = Image.open(getCardPath(cards[2]))
            self.cardimgp2 = ImageTk.PhotoImage(card_p2.resize((100,150), Image.ANTIALIAS))
            self.canvas.after(1750, lambda: self.canvas.create_image(350,250, anchor=tk.NW, image=self.cardimgp2))
            self.player_cardtot += getValue(cards[2])
            self.player_cards[2] = getValue(cards[2])

            #DEALER CARD 2
            card_d2 = Image.open(getCardPath(cards[3]))
            self.cardimgd2 = ImageTk.PhotoImage(card_d2.resize((100,150), Image.ANTIALIAS))
            self.canvas.after(2250, lambda: self.canvas.create_image(350,50, anchor=tk.NW, image=self.cardimgd2))
            self.dealer_cardtot += getValue(cards[3])

            #Display card total
            cardtottext = self.canvas.create_text(315, 410, anchor="nw")
            self.canvas.after(2500, lambda: self.canvas.itemconfig(cardtottext, text="Total: " +str(self.player_cardtot)
                                                                                    , font=("Verdana", 12), fill="white"))
            self.hit_times = 0

            self.hitsdic = {1:"hit1", 2:"hit2", 3:"hit3", 4:"hit4"} #make dic of variable names


            # Add card and update cards total
            def hitCard():


                #initialize counters
                self.hit_times += 1
                cardpull = self.hit_times + 3

                placex = 375 + (self.hit_times - 1)*40 #place cards beside each other
                card_p3 = Image.open(getCardPath(cards[cardpull]))
                self.hitsdic[self.hit_times] = ImageTk.PhotoImage(card_p3.resize((100,150), Image.ANTIALIAS))
                self.canvas.after(1000, lambda: self.canvas.create_image(placex,250, anchor=tk.NW, image=self.hitsdic[self.hit_times]))
                self.player_cardtot += getValue(cards[cardpull])
                self.player_cards[cardpull] = getValue(cards[cardpull])
                for i in self.player_cards:
                    print(self.player_cards[i])

                #check if player has ace, if total is >21, change ace value to 1
                checkcard = 0
                if getValue(cards[checkcard]) == 11 and self.player_cardtot > 21:
                    self.player_cardtot = self.player_cardtot - 10
                    self.acefound = True
                if checkcard<4:
                    checkcard+=2
                else:
                    checkcard+=1


                self.canvas.after(1000, lambda: self.canvas.itemconfig(cardtottext, text="Total: " +str(self.player_cardtot),
                                                                                        font=("Verdana", 12), fill="white"))

                #If player total is greater than 21
                if self.player_cardtot > 21:
                    playerBust()



            def standCard():
                print("test")


            def playerBust():
                busttext = self.canvas.create_text(310, 398, anchor="nw")
                self.canvas.after(1500, lambda: self.canvas.itemconfig(busttext, text="Bust", font=("Verdana", 30), fill="red"))

                #Destroy images and text
                self.canvas.after(1500, lambda: self.canvas.itemconfig(cardtottext, text=""))
                self.canvas.delete("self.cardimgp1")
                self.canvas.delete("self.cardimgp2")
                self.canvas.delete("self.cardimgd1")
                self.canvas.delete("self.cardimgd2")
                #for i in range(len(self.hitsdic)):
                #    self.canvas.delete(self.hitsdic[i])
                controller.show_frame(gamePage)


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
