from unittest import TestCase
from Game_Card.Card import Card


class TestCard(TestCase):
    def setUp(self):
        print("set up")

        self.a = Card("Diamond", 11)
        self.d = Card("Club", 10)

        self.b = Card(32, 'shimi')
        self.c = Card(5, 0)

        self.eq1 = Card('Heart', 5)
        self.eq2 = Card('Club', 5)
        self.eq3 = Card('Club', 2)
        self.eq4 = Card('Club', 2)

    def tearDown(self):
        print("tear down")

    def test___init__(self):
        # self.b = Card(32, 'shimi')  check invalid value,invalid suit
        self.assertTrue(self.b.suit == 'Diamond')
        self.assertTrue(self.b.value == 2)

        # self.c = Card(0,5)  check invalid value,invalid suit
        self.assertTrue(self.c.value == 2)
        self.assertTrue(self.c.suit == 'Diamond')

    def test___gt__(self):
        # self.a = Card("Diamond", 11)
        # self.d = Card("Club", 10)

        # self.eq1 = Card('Heart', 5)
        # self.eq2 = Card('Club', 5)
        # self.eq3 = Card('Club', 2)

        self.assertTrue(self.a.__gt__(self.d) is True)  # a> d True

        self.assertTrue(self.eq2.__gt__(self.eq1) is True)  # eq2>eq1 true

        self.assertTrue(self.eq1.__gt__(self.eq2) is False)  # eq1>eq2 false

        self.assertTrue(self.eq2.__gt__(self.eq3) is True)  # eq2>eq3 true

    def test___eq__(self):
        # self.eq2 = Card('Club', 5)
        # self.eq3 = Card('Club', 2)
        # self.eq4 = Card('Club',2)

        self.assertTrue(self.eq3.__eq__(self.eq4) is True)

        self.assertFalse(self.eq3.__eq__(self.eq2) is True)
