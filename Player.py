from Game_Card.DeckOfCards import DeckOfCards
from Game_Card.Card import Card
from random import randint


class Player:
    """The Player class holds information about player in card game"""

    def __init__(self, name, money=randint(5000, 10000), cards=5):
        if type(money) != int:
            money = 5000
        if money > 10000:
            money = 10000
        if money < 5000:
            money = 5000

        if cards > 13 or cards < 1:
            cards = 5
        if type(name) != str or len(name) < 1:
            name = 'Guest'

        self.cards = cards
        self.name = name
        self.money = money
        self.list_cards = []

    def __repr__(self):
        """Returns the details of the player"""
        return f'name: {self.name} money: {self.money} num cards: {len(self.list_cards)} cards: {self.list_cards}'

    def setHand(self, deck):
        """Gives deck of cards for player"""
        if len(deck.deck) > 0:
            for i in range(self.cards):
                self.list_cards.append(deck.deal_one())
        else:
            print('no more card in deck!')

    def getCard(self):
        """Return and remove random card from player """
        if len(self.list_cards) > 0:
            return self.list_cards.pop(randint(0, (len(self.list_cards) - 1)))
        else:
            print("no more cards in your deck!")

    def addCard(self, deck):
        """Add card from the deck to deck's player"""
        if len(deck.deck) > 0:
            self.list_cards.append(deck.deal_one())
        else:
            print("no more cards in deck!")

    def reduceAmount(self, amount):
        """Reduce money from player"""
        if amount < 0:
            amount = 0

        if self.money - amount <= 0:
            self.money = 0
        else:
            self.money -= amount

    def addAmount(self, amount):
        """Add money for player"""
        if amount < 0:
            amount = 0
        if self.money + amount >= 10000:
            self.money = 10000
        else:
            self.money += amount

    def print(self):
        """print details of player"""
        print(f'name: {self.name}  money: {self.money}  cards: {self.list_cards}')
