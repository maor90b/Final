from Game_Card.Card import Card
from random import shuffle


class DeckOfCards:
    """The DeckOfCards class holds a deck(list) of cards"""

    def __init__(self):
        self.deck = []
        values = [v for v in range(2, 15)]
        suits = ["Diamond", "Spade", "Heart", "Club"]
        for v in values:
            for s in suits:
                self.deck.append(Card(s, v))

    def __shuffle(self):
        """Shuffle the deck"""
        shuffle(self.deck)

    def deal_one(self):
        """Returns and remove the last card from the deck"""
        if 0 < len(self.deck) <= 52:
            return self.deck.pop()
        else:
            print("No more cards in deck!")

    def new_game(self):
        """Renew the deck, and shuffle it"""
        self.__init__()
        self.__shuffle()

    def show(self):
        """Print the deck"""
        print(self.deck)
