#the problem is to write a program that picks four cards randomly from a deck

# Create a deck of cards

# deckAllCards = list(range(52))
# same as one below

deckOfCards = []

for card in range(52):   #remember just because we have 52 doesnt mean 52 is a selected at all. Its 0 to 51. 51 example is 51//13 = 3.93 = 3(floor) = "Club"
    deckOfCards.append(card)
    
suits = ["Spade", "Hearts", "Diamonds", "Club"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Ace", "King", "Queen", "Jack"]

#shuffle the cards 
import random

# test
print (deckOfCards)
random.shuffle(deckOfCards)
print (deckOfCards)

# display the first four cards
print("The numbers for suit and rank for these 4 cards is: ")
for i in range(4):
    suit = suits[deckOfCards[i] // 13]
    rank = ranks[deckOfCards[i] % 13]
    print("Card number ",deckOfCards[i]," is a ", rank, " of ", suit)
    