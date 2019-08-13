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

values = [ "Ace", "2", "3", "4", "5", "6", "7","8", "9", "10", "Jack", "Queen", "King" ]
suits = [ "Clubs", "Diamonds", "Hearts", "Spades" ]

class Card:   
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit
    def show(self):
        print("{} of {}".format(self.suit, self.number))

class Deck:
    def __init__(self):
        self.cards = []
        self.build()
            
    def build(self): 
        for i in suits:
            for v in values:
                self.cards.append(Card(i, v))
        
    def show(self):
        for c in self.cards:
            c.show()
    
    def shuffle(self):
        for i in range(len(self.cards - 1, 0, -1)):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i] #<--This line creates the card swap by moving "K" to the end of the list in the shuffle algorithm
            
            
deck = Deck()
deck.shuffle()
deck.show()









