from Card import Card
from random import *


class DeckOfCards:

    def __init__(self):
        self.deck = [Card(v, s) for v in Card.value_list for s in Card.suit_list]

    def __str__(self):
        return f'my deck {self.deck}'

    def cards_shuffle(self):
        shuffle(self.deck)

    def deal_one(self):
        deal=choice(self.deck)
        self.deck.remove(deal)
        return deal


# deck=DeckOfCards()
#
# deck.cards_shuffle()
# print(deck)
#
# print(deck.deal_one())
# print(deck)
# deck.cards_shuffle()
# print(deck)

