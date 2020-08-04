from unittest import TestCase, mock
# from unittest.mock import patch
from Game_Card.Player import Player
from Game_Card.DeckOfCards import DeckOfCards
from Game_Card.Card import Card
from Game_Card.CardGame import CardGame


class TestCardGame(TestCase):
    def setUp(self):
        print("SetUp")

        self.d = DeckOfCards()

        self.p = Player('philips')

        self.war = CardGame()

    def tearDown(self):
        print("TearDown")

    def test___init__(self):
        self.war.__init__(7)
        self.assertTrue(self.war.players == 4)
        self.war.__init__(0)
        self.assertTrue(self.war.players == 2)

    def test_newGame(self):
        # self.war=CardGame()
        # self.d=DeckOfCards()
        self.assertFalse(self.war.list_players == [])
        self.war.deck.deck = []
        self.war.newGame()
        self.assertFalse(self.war.deck.deck == [])

        num = self.war.list_players[1].cards
        num2 = self.war.players
        self.assertEqual(len(self.war.deck.deck), len(self.d.deck) - (num * num2))

        for i in self.war.deck.deck:
            self.assertIn(i, self.d.deck)

        for p in self.war.list_players:
            for j in p.list_cards:
                self.assertIn(j, self.d.deck)

    def test_print(self):
        self.assertTrue(self.war.print()==print(self.war.list_players))
