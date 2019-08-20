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
#show probability of a 10
#allow multiple decks
import random


values = [ "Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King" ]
suits = [ "Clubs", "Diamonds", "Hearts", "Spades" ]


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

    def build(self):
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
            if i.number == "Ace" and 11 + total < 22:
                total += 11
            elif i.number == "Ace" and 11 + total > 22:
                total += 1
            elif type(i.number) == str:
                total += 10
        return(total)
     

def dealCards():
    player.draw(deck)
    dealer.draw(deck)
    print("Dealer's showing:")
    dealer.showHand()
    player.draw(deck)
    dealer.draw(deck)
        

def playerTurn():
    playerTotal = player.score()
    command = input("Type 'H' to hit or 'S' to stay: ".lower())
   
    while command == 'h' and playerTotal < 22:      
        player.draw(deck)
        playerTotal = player.score()
        print(playerTotal)
       
        if playerTotal < 22:       
            command = input("Type 'H' to hit or 'S' to stay: ".lower())
    
    player.showHand()
    print('Final score is {}'.format(playerTotal))


def dealerTurn():
    dealerTotal = dealer.score()
    
    while dealerTotal < 17:
        dealer.draw(deck)
        dealerTotal = dealer.score()
    
    print("Dealer's final score is {}".format(dealerTotal))
    dealer.showHand()


deck = Deck()
deck.shuffle()

player = Player("User")
dealer = Player("Dealer")
          
dealCards()

print("\nPlayer has:")
print(player.showHand())
print(player.score())

playerTurn()
dealerTurn()
    
