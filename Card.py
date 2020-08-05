class Card:
    """The Card class holds value and suit of certain card"""

    def __init__(self, suit, value):
        self.order = {"Diamond": 1, "Spade": 2, "Heart": 3, "Club": 4}
        if suit not in self.order:
            suit = "Diamond"

        if type(value) != int:
            value = 2
        elif value < 2 or value > 14:
            value = 2

        self.suit = suit
        self.value = value
        self.order = {"Diamond": 1, "Spade": 2, "Heart": 3, "Club": 4}

    def __repr__(self):
        """Returns the details of the card"""
        if self.value == 11:
            return f'J of {self.suit}'
        if self.value == 12:
            return f'Q of {self.suit}'
        if self.value == 13:
            return f'K of {self.suit}'
        if self.value == 14:
            return f'Ace of {self.suit}'

        return f'{self.suit} {self.value}'

    def __gt__(self, other):
        """Return greater card"""
        if self.value > other.value:
            return True
        if self.value == other.value:
            if self.order[self.suit] > other.order[other.suit]:
                return True
            return False

    def __eq__(self, other):
        """Return true for equal cards"""
        if self.value == other.value and self.suit == other.suit:
            return True
        return False
