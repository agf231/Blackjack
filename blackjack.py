# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 12:54:16 2019
@author: anfuente
"""
#Generate deck of cards
#Deal cards
#show dealt cards
#Create starting amount of money, keep track of it
#place/accept bets
#allow for hit, split, stay, doubledown
#play out dealer's hand
#determine winner
#add double option

#add split option
#show probability of a 10 -- will likely be its own function
#allow multiple decks -- create function create multiple objects and merge them


import random

values = [ "Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King" ]
suits = [ "Clubs", "Diamonds", "Hearts", "Spades" ]        
playerCash = 100   
bet = 0
playerTotal = 0

class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def show(self):
        print("{} of {}".format(self.number, self.suit))


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self, num):
        for s in suits:
            for v in values:
                self.cards.append(Card(v, s))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i] #<--This line creates the card swap by moving "K" to the end of the list in the shuffle algorithm

    def drawCard(self):
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()

    def score(self):
        total = 0
        for i in self.hand:
            if type(i.number) == int:
                total += i.number
            elif i.number == "Ace" and 11 + total < 22:
                total += 11
            elif type(i.number) == str:
                total += 10
        for i in self.hand:
            if i.number == "Ace" and total > 22:
                total -= 10
        return(total)
   
#----------------------------------------------------------------------------------------------
    
def placeBet():
    global bet
    global playerCash
    bet = int(input("How much would you like to wager? Minimum is 15. " ))
    try:
        if bet >= 15 and bet <= playerCash:
            playerCash -= bet
            return playerCash
        elif bet > playerCash:
            print("You can't wager more than you have, ya dingus.")
            placeBet()
        else:
            print("You must wager at least 15.")
            placeBet()
    except ValueError:
        print("You must input a number.")
        placeBet()
    return bet
    

def dealCards():
    player.draw(deck)
    dealer.draw(deck)
    print("Dealer's showing:")
    dealer.showHand()
    player.draw(deck)
    dealer.draw(deck)
    print("\nPlayer has:")
    player.showHand()
    player.score()
        

def playerTurn():
    global playerCash
    global bet
    global playerTotal 
    playerTotal = player.score()
    print(playerTotal)    
    command = input("Type 'H' to hit, 'S' to stay, or 'D' to double-down: ".lower())
   
    if command == 'h' and playerTotal < 22:      
        player.draw(deck)
        playerTotal = player.score()
        player.showHand()
        if playerTotal < 22:       
            playerTurn()
    elif command == 'd':
        if bet > playerCash:
            print("You don't have that much money.")
            playerTurn()
        else:
            playerCash -= bet
            bet += bet
            player.draw(deck)
            playerTotal = player.score()
            player.showHand()
    elif command == 's':
        player.showHand()
        pass
    else:
        print('Please enter a letter in accordance with the instructions.')
        playerTurn()
    return(playerTotal)


def dealerTurn():
    dealerTotal = dealer.score()
    
    while dealerTotal < 17:
        dealer.draw(deck)
        dealerTotal = dealer.score()
    
    print("\nDealer's final score is {}".format(dealerTotal))
    dealer.showHand()


def pickWinner(pTotal, dTotal):
    global playerCash
    global bet
    if pTotal == 21:
        print("\nBlackjack! Player wins!")
        playerCash += bet*2
    elif pTotal > 21:
        print("\nBust. Dealer wins.")
    elif dTotal > 21:
        print("\nDealer bust. Player wins.")
        playerCash += bet*2
    elif pTotal == dTotal:
        print("\nPush.")
        playerCash += bet
    elif pTotal > dTotal:
        print("\nPlayer wins.")
        playerCash += bet*2
    else:
        print("\nDealer wins.")   
    return playerCash

def chooseDecks():
    num = int(input("How many decks? Choose up to 10. "))
    if num > 10:
        print("That's too many decks.")
        chooseDecks()
    else:
        deck = Deck()*num
        deck.show()
        
#------------------------------------------------------------------------------------------------------------- 
chooseDecks()

while playerCash > 15:   
    deck = Deck()
    deck.shuffle()
    print("\nPlayer balance = 100.")
    
    player = Player("User")
    dealer = Player("Dealer")
    
    placeBet()    
    dealCards()
    
    playerTurn()
    print('Final score is {}'.format(playerTotal))
    dealerTurn()
    pickWinner(player.score(), dealer.score())
    print("\nPlayer balance is now {}.".format(playerCash))
    
    restart = input("Play again? Y/N ").lower()
    if restart != "y":
        break 

    
