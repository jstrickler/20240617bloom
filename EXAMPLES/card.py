
class Card:
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value):  # card.rank = "8" 
        self._rank = value

    @property
    def suit(self):
        return self._suit

    # how to reproduce the obj
    def __repr__(self):
        return f"Card('{self._rank}', '{self._suit}')"

    # info about the object
    def __str__(self):
        return f"{self.rank}-{self.suit}"

if __name__ == "__main__":
    c = Card('6', 'Diamonds')
    print(c)
    print(f"{c = }")
    c.rank = '9'
    print(c)

