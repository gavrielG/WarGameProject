from Player import *
class CardGame:
    def __init__(self,player1:str,player2:str,card_num1:int,card_num2:int):
        self.deck=DeckOfCards()
        self.player1=Player(player1,card_num1)
        self.player2=Player(player2,card_num2)
        self.new_game()


    def new_game(self):
        self.deck.cards_shuffle()
        self.player1.set_hand(self.deck)
        self.player2.set_hand(self.deck)


    def get_winner(self):
        if len(self.player1.playerdeck)==len(self.player2.playerdeck):
            return
        elif len(self.player1.playerdeck)>len(self.player2.playerdeck):
            return print(f'{self.player1.playername} is the winner!!')
        else:
            return print(f'{self.player2.playername} is the winner!!')



