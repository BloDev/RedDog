# Date: October 12, 2017
# Author: Brandon Lo
# Purpose: To play the game of Red Dog
# Inputs: Keyboard, parameters
# Output: Monitor/Screen
# =============================================================

import random
from tkinter import *
from tkinter import messagebox

# Date: October 13, 2017
# Author: Brandon Lo
# Purpose: To define two cards inside of a class
# Inputs: Sub getCard
# Output: Objects (card1, card2)
# =============================================================
class TwoCards():
    def __init__(self, card1, card2, suit1, suit2):
        self.card1 = card1
        self.card2 = card2
        self.suit1 = suit1
        self.suit2 = suit2

# Date: October 12, 2017
# Author: Brandon Lo
# Purpose: To determine the type of the card
# Inputs: No inputs
# Output: To return a random integer in range of 2 to 14
# =============================================================
def getCard():
    number = random.randint(2, 14)
    return number

# Date: October 16, 2017
# Author: Brandon Lo
# Purpose: To determine the suit of the card
# Inputs: No inputs
# Output: To return a random integer in range of 1 to 4
# =============================================================
def getSuit():
    number = random.randint(1, 4)
    return number

# Date: October 14, 2017
# Author: Brandon Lo
# Purpose: To get the two integer values from TwoCards, and make sure
#          that if they are the same value, that they have different suits
# Inputs: Class TwoCards, getCard
# Output: Returns the value of TwoCards
# =============================================================
def getHand():
    cards = TwoCards(getCard(), getCard(), getSuit(), getSuit())
    while (cards.card1 == cards.card2 and cards.suit1 == cards.suit2):
        cards = TwoCards(cards.card1, cards.card2, getSuit(), getSuit())
    return cards

# Date: October 27, 2017
# Author: Brandon Lo
# Purpose: Change the card values into their name (J, Q, K, A)
# Inputs: Parameter (card)
# Output: Returns the name of the card
# =============================================================
def cardDisplay(card):
    cardNumber = ""
    if (card == 11):
        cardNumber = "J"
    elif (card == 12):
        cardNumber = "Q"
    elif (card == 13):
        cardNumber = "K"
    elif (card == 14):
        cardNumber = "A"
    else:
        cardNumber = card
    return cardNumber

# Date: October 27, 2017
# Author: Brandon Lo
# Purpose: Display the suit on the cards
# Inputs: Parameter (sui)
# Output: Returns the suit of the card
# =============================================================

def suitDisplay(suit):
    cardSuit = ""
    if (suit == 1):
        cardSuit = "♦"
    elif (suit == 2):
        cardSuit = "♣"
    elif (suit == 3):
        cardSuit = "♥"
    else:
        cardSuit = "♠"
    return cardSuit

# Date: October 13, 2017
# Author: Brandon Lo
# Purpose: To show the user the cards
# Inputs: Class TwoCards, parameter (playerHand)
# Output: Screen/Monitor
# =============================================================
def printHand(playerHand):
    showCard1 = cardDisplay(playerHand.card1)
    displayCard1.set(showCard1)
    showSuit1 = suitDisplay(playerHand.suit1)
    if (showSuit1 == "♦" or showSuit1 == "♥"):
        displaySuit1.set(showSuit1)
        lblSuit1.config(fg = "red")
    else:
        displaySuit1.set(showSuit1)
        lblSuit1.config(fg = "black")
    showCard2 = cardDisplay(playerHand.card2)
    displayCard2.set(showCard2)
    showSuit2 = suitDisplay(playerHand.suit2)
    if (showSuit2 == "♦" or showSuit2 == "♥"):
        displaySuit2.set(showSuit2)
        lblSuit2.config(fg = "red")
    else:
        displaySuit2.set(showSuit2)
        lblSuit2.config(fg = "black")

# Date: October 17, 2017
# Author: Brandon Lo
# Purpose: Obtain the third card and make sure it does not have the
#          same suit as the other cards if it is the same value
# Inputs: Parameter (playerHand)
# Output: Returns the value of the third card
# =============================================================

def getThirdCard(playerHand):
    card1 = playerHand.card1
    card2 = playerHand.card2
    card3 = getCard()
    suit1 = playerHand.suit1
    suit2 = playerHand.suit2
    suit3 = getSuit()
    while (card1 == card3 and suit1 == suit3 or card2 == card3 and suit2 == suit3):
        suit3 = getSuit()
    showCard3 = cardDisplay(card3)
    displayCard3.set(showCard3)
    showSuit3 = suitDisplay(suit3)
    if (showSuit3 == "♦" or showSuit3 == "♥"):
        displaySuit3.set(showSuit3)
        lblSuit3.config(fg = "red")
    else:
        displaySuit3.set(showSuit3)
        lblSuit3.config(fg = "black")
    return card3

# Date: October 13, 2017
# Author: Brandon Lo
# Purpose: To determine the hand type of the received cards
# Inputs: Class TwoCards, parameter (playerHand)
# Output: Return card type
# =============================================================
def handType(playerHand):
    cardType = ""
    card1 = playerHand.card1
    card2 = playerHand.card2
    if (card1 == card2):
        cardType = "pair"
    elif (card1 == card2 + 1 or card1 + 1 == card2):
        cardType = "consecutive"
    else:
        cardType = "non-consecutive"
    return cardType

# Date: October 13, 2017
# Author: Brandon Lo
# Purpose: To determine the spread between two cards
# Inputs: Class TwoCards, parameter (playerHand)
# Output: Return card spread
# =============================================================
def spread(playerHand):
    cardSpread = 0
    card1 = playerHand.card1
    card2 = playerHand.card2
    if (card1 - 1 > card2):
        cardSpread = (card1 - 1) - card2
    elif (card2 - 1 > card1):
        cardSpread = (card2 - 1) - card1
    return cardSpread

# Date: October 13, 2017
# Author: Brandon Lo
# Purpose: To calculate the payout depending on the card spread
# Inputs: Class TwoCards, parameter (playerHand)
# Output: Return the card payout
# =============================================================
def payout(playerHand):
    cardPayout = 1
    cardSpread = spread(playerHand)
    if (cardSpread == 1):
        cardPayout = 5
    elif (cardSpread == 2):
        cardPayout = 4
    elif (cardSpread == 3):
        cardPayout = 2
    return cardPayout

# Date: October 13, 2017
# Author: Brandon Lo
# Purpose: To determine if the third card is in between the two cards
# Inputs: Parameters (playerHand, card2)
# Output: Return either true or false
# =============================================================
def between(playerHand, card3):
    card1 = playerHand.card1
    card2 = playerHand.card2
    valid = False
    if (card3 > card2 and card3 < card1) or (card3 > card1 and card3 < card2):
        valid = True
    return valid

# Date: October 26, 2017
# Author: Brandon Lo
# Purpose: To get the amount the player bets
# Inputs: Keyboard, parameters (checkMoney, prompt)
# Output: Return the bet value or shows an error
# =============================================================

def processBet(checkMoney):
    strUserInput = userBet.get()
    valid = 0
    if strUserInput.isdigit():
        intUserInput = int(strUserInput)
        if (intUserInput > 0 and intUserInput <= checkMoney):
            lblTitle.set("You have successfully bet $" + strUserInput + "!")
            valid = intUserInput
        else:
            messagebox.showerror("ERROR!", "Please enter a positive bet value that does not exceed $" + str(checkMoney) + ".")
            valid = 0
    else:
        messagebox.showerror("ERROR!", "Please enter a valid positive integer")
        valid = 0
    return valid

# Date: October 16, 2017
# Author: Brandon Lo
# Purpose: To check the maximum amount the user can bet
# Inputs: Sub userBet
# Output: Return the bet value
# =============================================================
def betMoney(purse, betAmount = 0):
    if (betAmount == 0):
        intBet = processBet(purse)
    else:
        if (purse < betAmount):
            intBet = processBet(purse)
        else:
            intBet = processBet(betAmount)
    return intBet

# Date: October 27, 2017
# Author: Brandon Lo
# Purpose: To ask if the user wants to bet again
# Inputs: Keyboard
# Output: Return the bet value & shows feedback
# =============================================================

def userInput(prompt = "Run again? (Y/N)"):
    lblBet.set(prompt)
    strUserInput = betAmount.get()
    if (strUserInput == "Y"  or strUserInput == "y" or strUserInput == "N" or strUserInput == "n"):
        lblTitle.set("Your balance has been resetted to $100.")
    else:
        messagebox.showerror("ERROR!", "Please enter either 'Y' or 'N'")
    return strUserInput
        

# Date: October 25, 2017
# Author: Brandon Lo
# Purpose: Gives an error message for using the menu
# Inputs: Mouse
# Output: Monitor/Screen
# =============================================================

def messagePopup(prompt = "This feature has not been implemented yet..."):
    messagebox.showinfo("Red Dog", prompt)

# Date: October 26, 2017
# Author: Brandon Lo
# Purpose: To allow the user to interact with the GUI
# Inputs: Keyboard
# Output: Monitor/Screen
# =============================================================

myWindow = Tk()

myWindow.title("Red Dog (GUI Version)")
myWindow.config(width = 825, height = 365, bg = "dark red")

userBet = StringVar()
userBet.set(value = "0")

lblTitle = StringVar()
lblTitle.set(value = "Welcome to Red Dog!")

lblBet = StringVar()
lblBet.set(value = "Enter Your Bet:")

lblBalance = StringVar()
lblBalance.set(value = "Your Balance: $100")

lblWins = StringVar()
lblWins.set(value = "Wins: 0")

lblLosses = StringVar()
lblLosses.set(value = "Losses: 0")

lblDraws = StringVar()
lblDraws.set(value = "Draws: 0")

lblTotalBet = StringVar()
lblTotalBet.set(value = "Total Bet: $0")

lblCardInfo = StringVar()
lblCardInfo.set(value = "")

displayCard1 = StringVar()
displayCard1.set(value = "")

displaySuit1 = StringVar()
displaySuit1.set(value = "?")

displayCard2 = StringVar()
displayCard2.set(value = "")

displaySuit2 = StringVar()
displaySuit2.set(value = "?")

displayCard3 = StringVar()
displayCard3.set(value = "")

displaySuit3 = StringVar()
displaySuit3.set(value = "?")

# MENU

menubar = Menu(myWindow)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label = "New", command = messagePopup)
filemenu.add_command(label = "Open", command = messagePopup)
filemenu.add_command(label = "Save", command = messagePopup)
filemenu.add_command(label = "Save as...", command = messagePopup)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = lambda: myWindow.destroy())
menubar.add_cascade(label = "File", menu = filemenu)

editmenu = Menu(menubar, tearoff = 0)
editmenu.add_command(label = "Undo", command = messagePopup)
menubar.add_cascade(label = "Edit", menu = editmenu)

helpmenu = Menu(menubar, tearoff = 0)
helpmenu.add_command(label = "Help Index", command = lambda: messagePopup("You must bet a valid amount that is greater than your current balance. Additional bets must not exceed your previous bet amount if you have enough in your balance."))
helpmenu.add_command(label = "About...", command = lambda: messagePopup("This program is created by Brandon Lo."))
menubar.add_cascade(label = "Help", menu = helpmenu)

myWindow.config(menu = menubar)

# Title
Label(myWindow, textvariable = lblTitle, width = 27, height = 4, wraplength = 250, justify = "left", bg = "dark red", fg = "white", font = ("Gothic", 12, "bold")).place(x = 25.5, y = 10)

# Bet Frame
frmBet = Frame(myWindow, width = 250, height = 210, bg = "dark red", highlightbackground = "white", highlightthickness = 2).place(x = 25, y = 80)
Label(frmBet, textvariable = lblBalance, bg = "dark red", fg = "white", font = ("Gothic", 12, "bold")).place(x = 40, y = 100)
Label(frmBet, textvariable = lblBet, bg = "dark red", fg = "white", font = ("Gothic", 12, "bold")).place(x = 40, y = 140)
Entry(frmBet, textvariable = userBet, width = 8, bg = "dark red", fg = "white", highlightthickness = 2, relief = "solid", font = ("Gothic", 12)).place(x = 190, y = 140)
buttonBet = Button(frmBet, text = "Bet", font = ("Helvetica", 12, "bold"), width = 22, height = 1, command = lambda: userClickBet())
buttonBet.place(x = 35, y = 180)
buttonAdditionalBet = Button(frmBet, text = "Additional Bet", font = ("Helvetica", 12, "bold"), state = "disabled", width = 22, height = 1, command = lambda: userClickAdditionalBet())
buttonAdditionalBet.place(x = 35, y = 215)
buttonPass = Button(frmBet, text = "Pass", font = ("Helvetica", 12, "bold"), state = "disabled", width = 11, height = 1, command = lambda: userClickPass())
buttonPass.place(x = 35, y = 250)
buttonReset = Button(frmBet, text = "Reset", font = ("Helvetica", 12, "bold"), width = 10, height = 1, command = lambda: userClickReset())
buttonReset.place(x = 155, y = 250)

# Information
Label(frmBet, textvariable = lblWins, bg = "dark red", fg = "white", font = ("Gothic", 12, "bold")).place(x = 25, y = 300)
Label(frmBet, textvariable = lblLosses, bg = "dark red", fg = "white", font = ("Gothic", 12, "bold")).place(x = 25, y = 330)
Label(frmBet, textvariable = lblDraws, bg = "dark red", fg = "white", font = ("Gothic", 12, "bold")).place(x = 150, y = 300)
Label(frmBet, textvariable = lblTotalBet, bg = "dark red", fg = "white", font = ("Gothic", 12, "bold")).place(x = 150, y = 330)

# Card Frame
frmCard = Frame(myWindow, width = 500, height = 275, bg = "green").place(x = 300, y = 25)

# Card 1 Image
frmCard1 = Frame(frmCard, width = 140, height = 200, bg = "white", highlightbackground = "black", highlightthickness = 5).place(x = 325, y = 45)
Label(frmCard1, textvariable = displayCard1, bg = "white", font = ("Helvetica", 24, "bold")).place(x = 335, y = 50)
lblSuit1 = Label(frmCard1, textvariable = displaySuit1, bg = "white", font = ("Helvetica", 65, "bold"))
lblSuit1.place(x = 365, y = 90)
Label(frmCard, text = "First Card", font = ("Gothic", 12, "bold"), fg = "light green", bg = "green").place(x = 345, y = 260)

# Card 2 Image
frmCard2 = Frame(frmCard, width = 140, height = 200, bg = "white", highlightbackground = "black", highlightthickness = 5).place(x = 482.5, y = 45)
Label(frmCard2, textvariable = displayCard2, bg = "white", font = ("Helvetica", 24, "bold")).place(x = 492.5, y = 50)
lblSuit2 = Label(frmCard2, textvariable = displaySuit2, bg = "white", font = ("Helvetica", 65, "bold"))
lblSuit2.place(x = 525, y = 90)
Label(frmCard, text = "Second Card", font = ("Gothic", 12, "bold"), fg = "light green", bg = "green").place(x = 500, y = 260)

# Card 3 Image
frmCard3 = Frame(frmCard, width = 140, height = 200, bg = "white", highlightbackground = "black", highlightthickness = 5).place(x = 640, y = 45)
Label(frmCard3, textvariable = displayCard3, bg = "white", font = ("Helvetica", 24, "bold")).place(x = 650, y = 50)
lblSuit3 = Label(frmCard3, textvariable = displaySuit3, bg = "white", font = ("Helvetica", 65, "bold"))
lblSuit3.place(x = 680, y = 90)
Label(frmCard, text = "Third Card", font = ("Gothic", 12, "bold"), fg = "light green", bg = "green").place(x = 670, y = 260)

# Card Text
Label(myWindow, textvariable = lblCardInfo, width = 55, height = 2, wraplength = 510, justify = "left", bg = "dark red", fg = "white", font = ("Gothic", 12, "bold")).place(x = 300, y = 315)


# Initialization (Had to use global variables for functions to see outside of scope)
purse = 100
totalBet = 0
losses = 0
wins = 0
draws = 0
amountBet = 0

# Date: October 27, 2017
# Author: Brandon Lo
# Purpose: Allows the user to reset the game
# Inputs: Mouse
# Output: Monitor/Screen
# =============================================================

def userClickReset():
    global purse
    global losses
    global wins
    global draws
    global amountBet

    purse = 100
    losses = 0
    wins = 0
    draws = 0
    amountBet = 0

    lblTitle.set("The game has been reset. You now have $100 in your balance.")
    lblBalance.set("Your Balance: $100")
    lblCardInfo.set("")
    lblDraws.set("Draws: 0")
    lblWins.set ("Wins: 0")
    lblLosses.set("Losses: 0")
    lblTotalBet.set("Total Bet: $0")
    lblBet.set("Enter Your Bet:")
    userBet.set(value = "0")

    buttonPass.config(state = "disabled")
    buttonAdditionalBet.config(state = "disabled")
    buttonBet.config(state = "active")

    displayCard1.set(value = "")
    displaySuit1.set(value = "?")
    lblSuit1.config(fg = "black")

    displayCard2.set(value = "")
    displaySuit2.set(value = "?")
    lblSuit2.config(fg = "black")

    displayCard3.set(value = "")
    displaySuit3.set(value = "?")
    lblSuit3.config(fg = "black")

# Date: October 27, 2017
# Author: Brandon Lo
# Purpose: Allows the enter their bet
# Inputs: Mouse/Keyboard
# Output: Monitor/Screen
# =============================================================

def userClickBet():
    global purse
    global losses
    global wins
    global draws
    global betAmount
    global playerHand
    global amountBet

    displayCard3.set("")
    displaySuit3.set("?")
    lblSuit3.config(fg = "black")
    
    betAmount = betMoney(purse, 0)
    
    if betAmount > 0:
        playerHand = getHand()
        printHand(playerHand)
        handSet = handType(playerHand)

        userBet.set(value = "0")
        lblBet.set("Enter Your Bet:")
        amountBet += betAmount
        lblTotalBet.set("Total Bet: $" + str(amountBet))
        
        if (handSet == "pair"):
            thirdCard = getThirdCard(playerHand)
            
            if (thirdCard == playerHand.card1):
                purse += betAmount * 11
                lblTitle.set("You have just won " + str(betAmount * 11) + "!")
                lblCardInfo.set("You have matched all three pairs!")
                wins += 1
                lblWins.set("Wins: " + str(wins))
                lblBalance.set("Your Balance: $" + str(purse))
            else:
                lblCardInfo.set("You have a pair, but the third card did not match. It was a tie...")
                lblTitle.set("Please re-enter another bet value.")
                draws += 1
                lblDraws.set("Draws: " + str(draws))
                
        elif (handSet == "consecutive"):
            lblCardInfo.set("You have a consecutive hand. It was a tie...")
            lblTitle.set("Please re-enter another bet value.")
            draws += 1
            lblDraws.set("Draws: " + str(draws))
            
        else:
            lblBalance.set("Your Balance: $" + str(purse - betAmount))
            lblCardInfo.set("You have a non-consecutive hand. Enter an additional bet ($1 - $" + str(betAmount) + ") or choose to pass.")
            lblBet.set("Additional Bet:")
            buttonBet.config(state = "disabled")
            userBet.set(value = "0")
            
            if (purse - betAmount != 0):
                buttonAdditionalBet.config(state = "active")
                buttonPass.config(state = "active")
            else:
                userClickPass()

# Date: October 27, 2017
# Author: Brandon Lo
# Purpose: Allows the user to enter an additional bet
# Inputs: Mouse/Keyboard
# Output: Monitor/Screen
# =============================================================

def userClickAdditionalBet():
    global purse
    global playerHand
    global wins
    global losses
    global amountBet

    additionalBetAmount = betMoney((purse - betAmount), betAmount)

    if (additionalBetAmount > 0):

        totalBet = betAmount + additionalBetAmount
        amountBet += additionalBetAmount
        lblTotalBet.set("Total Bet: $" + str(amountBet))

        lblTitle.set("You have chose to bet an additional $" + str(additionalBetAmount) + ".")
        thirdCard = getThirdCard(playerHand)
        if (between(playerHand, thirdCard) == True):
            purse = purse + totalBet * payout(playerHand)
            lblCardInfo.set("Your third card was in between your first two cards... You have just won $" + str(totalBet * payout(playerHand)) + "!")
            wins += 1
            lblWins.set("Wins: " + str(wins))
            
        else:
            purse -= totalBet
            lblCardInfo.set("Your third card was not in between your first two cards... You have just lost $" + str(totalBet) + ".")
            losses += 1
            lblLosses.set("Losses: " + str(losses))
            
        lblBalance.set("Your Balance: $" + str(purse))
        buttonPass.config(state = "disabled")
        buttonAdditionalBet.config(state = "disabled")
        userBet.set(value = "0")

        if purse != 0:
            buttonBet.config(state = "active")
        else:
            buttonBet.config(state = "disabled")
            lblTitle.set("Sorry, but you have no money left in your balance. Click 'Reset' to restart the game.")

        lblBet.set("Enter Your Bet:")

# Date: October 27, 2017
# Author: Brandon Lo
# Purpose: Allows the user to skip on an additional bet
# Inputs: Mouse/Keyboard
# Output: Monitor/Screen
# =============================================================

def userClickPass():
    global purse
    global playerHand
    global wins
    global losses
    global amountBet

    lblTitle.set("You have skipped on the additional bet.")
    thirdCard = getThirdCard(playerHand)
    
    if (between(playerHand, thirdCard) == True):
        purse = purse + betAmount * payout(playerHand)
        lblCardInfo.set("Your third card was in between your first two cards... You have just won $" + str(betAmount * payout(playerHand)) + "!")
        wins += 1
        lblWins.set("Wins: " + str(wins))
        lblBalance.set("Your Balance: $" + str(purse))
        
    else:
        purse -= betAmount
        lblCardInfo.set("Your third card was not in between your first two cards... You have just lost $" + str(betAmount) + ".")
        losses += 1
        lblLosses.set("Losses: " + str(losses))
        lblBalance.set("Your Balance: $" + str(purse))

    buttonPass.config(state = "disabled")
    buttonAdditionalBet.config(state = "disabled")
    lblBet.set("Enter Your Bet:")
    userBet.set(value = "0")

    if purse != 0:
        buttonBet.config(state = "active")
    else:
        buttonBet.config(state = "disabled")
        lblTitle.set("Sorry, but you have no money left in your balance. Click 'Reset' to restart the game.")

mainloop()
