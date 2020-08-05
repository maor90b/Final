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
        self.p3 = Player(5, 50000,'str')
        self.p4 = Player('mike', -5, -1)
        self.p5 = Player('Dude', 'str', 20)

    def tearDown(self):
        print('TearDown')

    def test___init(self):
        # self.p3=Player(5,50000)
        self.assertTrue(self.p3.money == 10000)
        self.assertTrue(self.p3.name == 'Guest')
        self.assertTrue(self.p3.cards==5)

        # self.p4 = Player('mike',-5,-1)
        self.assertTrue(self.p4.money == 5000)
        self.assertTrue(self.p4.cards == 5)

        # self.p5=Player('Dude','str',20)  invalid money, invalid
        self.assertTrue(self.p5.money == 5000)
        self.assertTrue(self.p5.cards == 5)

    def test_setHand(self):
        # self.d = DeckOfCards()
        # self.d2 = DeckOfCards()
        # self.p = Player('maor')

        self.p.setHand(self.d)

        for i in self.p.list_cards:
            for j in self.d.deck:
                self.assertFalse(i == j)
        self.assertTrue(len(self.d.deck) == len(self.d2.deck) - 5)
        self.assertTrue(len(self.p.list_cards) == 5)

        for a in self.p.list_cards:
            self.assertTrue(type(a) == Card)

        for i in range(10):
            self.p.setHand(self.d)

        self.assertTrue(self.p.setHand(self.d) == print('no more card in deck!'))

    def test_getCard(self):
        # self.p = Player('maor')
        # self.p2 = Player('philips')
        self.p.setHand(self.d)
        self.p2.setHand(self.d)

        self.p2.getCard()
        self.assertTrue(len(self.p2.list_cards) == (len(self.p.list_cards) - 1))

        for i in range(len(self.p2.list_cards) + 1):
            self.p2.getCard()
        self.assertTrue(len(self.p2.list_cards) == 0)

    def test_addCard(self):
        #     self.p = Player('maor')
        #     self.p2 = Player('philips')
        #     self.d = DeckOfCards()

        self.p.setHand(self.d)
        self.p2.setHand(self.d)

        self.p2.addCard(self.d)
        self.assertTrue(len(self.p.list_cards) + 1 == len(self.p2.list_cards))
        #
        #     self.p3 = Player('mike')
        #     self.d2 = DeckOfCards
        #     self.d3=DeckOfCards()
        for i in range(100):
            self.p3.addCard(self.d2)

        print(self.p3.list_cards)
        print(len(self.p3.list_cards))

        self.assertEqual(len(self.p3.list_cards), len(self.d3.deck))

        self.assertTrue(self.p3.addCard(self.d2) == print("no more cards in deck!"))

    def test_reduceAmount(self):
        # self.p = Player('maor')
        self.p.reduceAmount(80000)
        self.assertTrue(self.p.money == 0)

        cash = self.p2.money
        self.p2.reduceAmount(-5)
        self.assertTrue(self.p2.money == cash)

        cash -= 100
        self.p2.reduceAmount(100)
        self.assertTrue(cash == self.p2.money)

    def test_addAmount(self):

        # self.p2 = Player('philips')
        print(self.p2.money)
        amount = self.p2.money
        self.p2.addAmount(-1)
        self.assertTrue(self.p2.money == amount)

        self.p2.addAmount(10001)
        self.assertTrue(self.p2.money == 10000)

        cash = 10001
        self.p2.addAmount(1)
        self.assertFalse(self.p2.money == cash)

    def test_print(self):
        self.assertTrue(self.p.print()==print(f'name: {self.p.name}  money: {self.p.money}  cards: {self.p.list_cards}'))


