import tkinter as tk
from PIL import ImageTk, Image

deck = {
  1:"AC",2:"2C",3:"3C",4:"4C",5:"5C",6:"6C",7:"7C",8:"8C",9:"9C",
  10:"10C",11:"JC",12:"QC",13:"KC",
  14:"AS",15:"2S",16:"3S",17:"4S",18:"5S",19:"6S",20:"7S",21:"8S",22:"9S",
  23:"10S",24:"JS",25:"QS",26:"KS",
  27:"AH",28:"2H",29:"3H",30:"4H",31:"5H",32:"6H",33:"7H",34:"8H",35:"9H",
  36:"10H",37:"JH",38:"QH",39:"KH",
  40:"AD",41:"2D",42:"3D",43:"4D",44:"5D",45:"6D",46:"7D",47:"8D",48:"9D",
  49:"10D",50:"JD",51:"QD",52:"KD"
}


def getCardPath(card):
    path = "Images\\Cards\\" + deck[card] + ".png"
    return path



def getValue(card):
    cardset = setCard(card)
    value = setVal(cardset)
    return value

def setCard(card):
    if card <=13:
        cardset = card
    elif card > 13 and card<=26:
        cardset = card - 13
    elif card > 26 and card<=39:
        cardset = card - 26
    elif card > 39 and card <= 53:
        cardset = card - 39

    return cardset


def setVal(cardset):
    if cardset == 1:
        cardval = 11
    elif cardset >=2 and cardset<10:
        cardval = cardset
    elif cardset >=10 and cardset<=13:
        cardval = 10

    return cardval
