import unittest

from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard


class TestCardRepository(unittest.TestCase):
    def test_init_attr(self):
        cr = CardRepository()
        self.assertEqual(cr.count, 0)
        self.assertEqual(cr.cards, [])

    def test_add_existing_card_raises(self):
        cr = CardRepository()
        c1 = MagicCard('magic')
        c2 = MagicCard('magic')
        cr.add(c1)

        with self.assertRaises(ValueError) as content:
            cr.add(c2)

        self.assertEqual(str(content.exception), f"Card {c2.name} already exists!")

    def test_add_with_valid_data(self):
        cr = CardRepository()
        c = MagicCard('magic')
        cr.add(c)

        result = [c]

        self.assertEqual(cr.cards, result)
        self.assertEqual(cr.count, 1)

    def test_remove_with_empty_string_raises(self):
        cr = CardRepository()
        with self.assertRaises(ValueError) as content:
            cr.remove("")

        self.assertEqual(str(content.exception), "Card cannot be an empty string!")

    def test_remove_with_valid_data(self):
        cr = CardRepository()
        cr.add(MagicCard('magic'))

        result = []
        cr.remove("magic")

        self.assertEqual(cr.cards, result)
        self.assertEqual(cr.count, 0)

    def test_find(self):
        cr = CardRepository()
        c = MagicCard('magic')
        cr.add(c)

        result = c

        self.assertEqual(cr.find('magic'), result)
