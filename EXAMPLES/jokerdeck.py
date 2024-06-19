from carddeck import CardDeck, Card

JOKER = '\U0001F0CF'

class Game:
    def play(self):
        print("Playing")

class JokerDeck(CardDeck, Game):

    def _make_deck(self):
        super()._make_deck()  # call _make_deck() in parent
        for _ in range(2):
            card = Card("JOKER", JOKER)
            self._cards.append(card)

if __name__ == "__main__":
    j = JokerDeck("Jimmy")
    j.shuffle()
    print(j.cards)
    j.play()