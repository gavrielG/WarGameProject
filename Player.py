from DeckOfCards import *
class Player:
    def __init__(self,playername:str,card_num:int=26):
        if card_num < 10 or card_num > 26:
            card_num = 26
        if type(card_num) != int:
            raise TypeError('Cards number must be int')
        if type(playername) != str:
            raise TypeError('Player name must be str')
        self.playerdeck=[]
        self.playername=playername
        self.card_num=card_num



    def __str__(self):
        return f'Player deck :{self.playerdeck}'

    def set_hand(self, deck:DeckOfCards):
        if type(deck)!=DeckOfCards:
            raise TypeError('Deck must be DeckOfCards type')
        for i in range(self.card_num):
            deleted=deck.deal_one()
            self.add_card(deleted)

    def get_card(self):
        a=choice(self.playerdeck)
        self.playerdeck.remove(a)
        return a


    def add_card(self,card:Card):
        if type(card)!=Card:
            raise TypeError('Card must be type card')
        if card in self.playerdeck:
            return 'Card is already in player deck'
        self.playerdeck.append(card)

# deck=DeckOfCards()
# player1=Player('gavriel',15)
# player2=Player('natan',15)
# player2.set_hand(deck)
# player1.set_hand(deck)
# print(player1.playerdeck)
# print(player2.playerdeck)


