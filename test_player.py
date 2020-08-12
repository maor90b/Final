from unittest import TestCase, mock
# from unittest.mock import patch
from Game_Card.Player import Player
from Game_Card.DeckOfCards import DeckOfCards
from Game_Card.Card import Card


# from Game_Card2.Card import Card

class TestPlayer(TestCase):

    def setUp(self):
        print('setup')
        self.d = DeckOfCards()
        self.d2 = DeckOfCards()
        self.d3 = DeckOfCards()

        self.p = Player('maor')
        self.p2 = Player('philips')
        self.p3 = Player(5, 50000, 'str')
        self.p4 = Player('mike', -5, -1)
        self.p5 = Player('Dude', 'str', 20)

    def tearDown(self):
        print('TearDown')

    def test___init(self):
        # self.p3=Player(5,50000,'str')  invalid name,invalid :money<5000, invalid num cards
        self.assertTrue(self.p3.money == 10000)
        self.assertTrue(self.p3.name == 'Guest')
        self.assertTrue(self.p3.cards == 5)

        # self.p4 = Player('mike',-5,-1)   # money<0, num cards<0
        self.assertTrue(self.p4.money == 5000)
        self.assertTrue(self.p4.cards == 5)

        # self.p5=Player('Dude','str',20)  invalid money, if cards>13
        self.assertTrue(self.p5.money == 5000)
        self.assertTrue(self.p5.cards == 5)

    def test_setHand(self):
        # self.d = DeckOfCards()
        # self.d2 = DeckOfCards()
        # self.p = Player('maor')

        self.p.setHand(self.d)

        for i in self.p.list_cards:
            for j in self.d.deck:
                self.assertFalse(i == j)  # check if card in player deck in DeckOfCards==False
        self.assertTrue(len(self.d.deck) == len(self.d2.deck) - 5)
        self.assertTrue(len(self.p.list_cards) == 5)

        for a in self.p.list_cards:  # check if all the items in list is type Card
            self.assertTrue(type(a) == Card)

        for i in range(20):  # check if there is a limit of set hand
            self.p.setHand(self.d)
        self.assertTrue(len(self.p.list_cards) == len(self.d2.deck))  # check if len DeckOfCards== len playr listcards

        for c in self.p.list_cards:  # check if the cards in both list are the same card
            self.assertIn(c, self.d2.deck)

        self.assertTrue(self.p.setHand(self.d) == print('no more card in deck!'))  # if len of deck >0 =false

    def test_getCard(self):
        # self.p = Player('maor')
        # self.p2 = Player('philips')
        self.p.setHand(self.d)
        self.p2.setHand(self.d)

        self.p2.getCard()
        self.assertTrue(len(self.p2.list_cards) == (
                    len(self.p.list_cards) - 1))  # check if get card delete a card from player's list

        for i in range(len(self.p2.list_cards) + 1):
            self.p2.getCard()
        self.assertTrue(len(self.p2.list_cards) == 0)  # check if get card out of range cant happend

    def test_addCard(self):
        #     self.p = Player('maor')
        #     self.p2 = Player('philips')
        #     self.d = DeckOfCards()

        self.p.setHand(self.d)
        self.p2.setHand(self.d)

        self.p2.addCard(self.d)
        self.assertTrue(
            len(self.p.list_cards) + 1 == len(self.p2.list_cards))  # check if 1 card from deck goes to player

        #     self.p3 = Player('mike')
        #     self.d2 = DeckOfCards
        #     self.d3=DeckOfCards()
        for i in range(len(self.d2.deck) + 1):  # check if out of range cant doesnt return something to deck
            self.p3.addCard(self.d2)

        # print(self.p3.list_cards)
        # print(len(self.p3.list_cards))

        self.assertEqual(len(self.p3.list_cards), len(
            self.d3.deck))  # check if len(player cards) after addcard in range out of range = len DeckOfcards

        self.assertTrue(self.p3.addCard(self.d2) == print("no more cards in deck!"))

    def test_reduceAmount(self):
        # self.p = Player('maor')
        self.p.reduceAmount(80000)  # check if money -amount <0 then = 0
        self.assertTrue(self.p.money == 0)

        cash = self.p2.money
        self.p2.reduceAmount(-5)  # check if amount<0 then amount = 0
        self.assertTrue(self.p2.money == cash)

        cash -= 100
        self.p2.reduceAmount(100)  # caheck if reduce amount works
        self.assertTrue(cash == self.p2.money)

    def test_addAmount(self):

        # self.p2 = Player('philips')
        print(self.p2.money)
        amount = self.p2.money
        self.p2.addAmount(-1)  # check if amount<0 then amount=0
        self.assertTrue(self.p2.money == amount)

        self.p2.addAmount(10001)  # check if money+amount>10000 then money = 10000
        self.assertTrue(self.p2.money == 10000)

        cash = 10001
        self.p2.addAmount(1)  # check if money+amount>10000 then money = 10000
        self.assertFalse(self.p2.money == cash)

        self.p2.money = 5000
        self.p2.addAmount(500)
        self.assertTrue(self.p2.money == 5500)  # check if add amount works

    def test_print(self):
        self.assertTrue(
            self.p.print() == print(f'name: {self.p.name}  money: {self.p.money}  cards: {self.p.list_cards}'))
