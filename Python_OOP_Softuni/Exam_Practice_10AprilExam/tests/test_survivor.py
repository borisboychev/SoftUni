import unittest

from project.survivor import Survivor


class TestSurvivor(unittest.TestCase):
    def test_name_with_empty_string_should_raise_exception(self):
        with self.assertRaises(ValueError) as content:
            s = Survivor('', 12)

        self.assertEqual(str(content.exception), "Name not valid!")

    def test_name_with_valid_input(self):
        s = Survivor('test', 12)
        result = s.name

        self.assertEqual(result, 'test')

    def test_age_with_value_less_than_zero_should_raise_exception(self):
        with self.assertRaises(ValueError) as content:
            s = Survivor('test', -1)

        self.assertEqual(str(content.exception), 'Age not valid!')

    def test_age_with_valid_input(self):
        s = Survivor('test', 12)
        result = s.age

        self.assertEqual(result, 12)

    def test_health_with_value_greater_than_100(self):
        s = Survivor('test', 12)
        s.health = 101

        self.assertEqual(s.health, 100)

    def test_health_with_value_less_than_0(self):
        s = Survivor('test', 12)
        with self.assertRaises(ValueError) as content:
            s.health = -1

    def test_needs_with_value_greater_than_100(self):
        s = Survivor('test', 12)
        s.needs = 101

        self.assertEqual(s.needs, 100)

    def test_needs_with_value_less_than_0(self):
        s = Survivor('test', 12)
        with self.assertRaises(ValueError) as content:
            s.needs = -1

        self.assertEqual(str(content.exception), "Needs not valid!")

    def test_need_healing_with_health_equal_to_100(self):
        s = Survivor('test', 12)
        s.health = 100
        result = s.needs_healing

        self.assertEqual(result, False)

    def test_need_healing_with_health_less_than_100(self):
        s = Survivor('test', 12)
        s.health -= 50
        result = s.needs_healing

        self.assertEqual(result, True)

    def test_needs_sustenance_with_needs_equal_to_100(self):
        s = Survivor('test', 12)
        s.needs = 100
        result = s.needs_sustenance

        self.assertEqual(result, False)

    def test_need_sustolics_with_needs_less_than_100(self):
        s = Survivor('test', 12)
        s.needs -= 50
        result = s.needs_sustenance

        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()
