import unittest

from project.factory.paint_factory import PaintFactory


class TestPainFactory(unittest.TestCase):
    def test_init_attr(self):
        pf = PaintFactory('Test', 10)

        self.assertEqual(pf.name, 'Test')
        self.assertEqual(pf.capacity, 10)
        self.assertEqual(pf.__class__.__name__, 'PaintFactory')

    def test_add_ingredient_with_invalid_type(self):
        pf = PaintFactory('Test', 10)

        with self.assertRaises(TypeError) as content:
            pf.add_ingredient('orange', 1)

        self.assertEqual(str(content.exception), "Ingredient of type orange not allowed in PaintFactory")

    def test_add_ingredient_with_invalid_quantity(self):
        pf = PaintFactory('Test', 10)

        with self.assertRaises(ValueError) as content:
            pf.add_ingredient('red', 11)

        self.assertEqual(str(content.exception), "Not enough space in factory")

    def test_add_ingredient_with_valid_input(self):
        pf = PaintFactory('Test', 10)

        pf.add_ingredient('red', 4)

        self.assertEqual(pf.products, {'red': 4})

    def test_remove_ingredient_with_invalid_ingredient(self):
        pf = PaintFactory('Test', 10)
        pf.add_ingredient('red', 4)

        with self.assertRaises(KeyError) as content:
            pf.remove_ingredient('orange', 4)

        self.assertEqual(str(content.exception).strip('\''), "No such ingredient in the factory")

    def test_remove_ingredient_with_invalid_quantity(self):
        pf = PaintFactory('Test', 10)
        pf.add_ingredient('red', 4)

        with self.assertRaises(ValueError) as content:
            pf.remove_ingredient('red', 5)

        self.assertEqual(str(content.exception), "Ingredient quantity cannot be less than zero")

    def test_remove_ingredient_with_valid_input(self):
        pf = PaintFactory('Test', 10)
        pf.add_ingredient('red', 4)
        pf.remove_ingredient('red', 2)

        self.assertEqual(pf.products, {'red': 2})

    def test_property_products(self):
        pf = PaintFactory('Test', 10)
        pf.add_ingredient('red', 4)

        self.assertEqual(pf.products, pf.ingredients)