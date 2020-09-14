class CardRepository:
    def __init__(self):
        self.count = 0
        self.cards = []

    def add(self, card):

        names = [c.name for c in self.cards]
        if card.name in names:
            raise ValueError(f"Card {card.name} already exists!")

        self.cards.append(card)
        self.count += 1

    def remove(self, card):
        if card == "":
            raise ValueError("Card cannot be an empty string!")
        card_to_remove = [c for c in self.cards if c.name == card][0]
        self.cards.remove(card_to_remove)
        self.count -= 1

    def find(self, name):
        c = [c for c in self.cards if c.name == name][0]
        return c