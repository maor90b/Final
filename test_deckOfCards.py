from unittest import TestCase
from unittest.mock import patch
from Game_Card.DeckOfCards import DeckOfCards
from Game_Card.Card import Card


class TestDeckOfCards(TestCase):

    def setUp(self):
        print('setup')
        self.d = DeckOfCards()
        self.d2 = DeckOfCards()
        self.d3 = DeckOfCards()

    def tearDown(self):
        print('TearDown')

    def test_deal_one(self):
        self.assertTrue(self.d.deck[-1] == self.d.deal_one())

        card = self.d.deal_one()
        self.assertTrue(type(card) == Card)

        for i in range(len(self.d.deck)):
            self.d.deal_one()
        self.assertTrue(self.d.deck == [])
        self.assertTrue(len(self.d.deck) == 0)
        self.assertTrue(self.d.deal_one() == print('No more cards in deck!'))

    def test_new_game(self):
        self.d.new_game()

        # self.d2 = DeckOfCards()
        self.assertTrue(len(self.d.deck) == 52)
        for i in self.d.deck:
            self.assertIn(i, self.d2.deck)

        count = 0
        for i in range(len(self.d.deck)):
            if self.d.deck[i] == self.d2.deck[i]:
                count += 1
        print(count)
        self.assertGreater(len(self.d.deck), count)

    def test_show(self):
        pass
