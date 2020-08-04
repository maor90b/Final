from Game_Card.DeckOfCards import DeckOfCards
from Game_Card.Card import Card
from Game_Card.Player import Player
from random import randint


class CardGame:
    """This class holds information about players, and deck"""

    def __init__(self, players=4):
        if players > 4:
            players = 4
        if players < 2:
            players = 2
        self.deck = DeckOfCards()
        self.players = players
        self.list_players = []
        self.newGame()

    def print(self):
        """print list of the players"""
        print(self.list_players)

    def newGame(self):
        """Renew and shuffle the deck, and gives cards for the players"""
        self.list_players = []
        self.deck.new_game()
        for i in range(self.players):
            p = Player(input('enter name: '))
            p.setHand(self.deck)
            self.list_players.append(p)

        # for i in range(len(self.list_players)):
        #     self.list_players[i].setHand(self.deck)

# war = CardGame()
# print(len(war.deck.deck))
# war.newGame()
# war.print()
#
# poker = CardGame()
#
# poker.print()
