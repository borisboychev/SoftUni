import unittest
from person import Person


class TestPerson(unittest.TestCase):
    def test_valid_name_and_valid_age_should_greet(self):
        name = 'testuser'
        age = 12

        p = Person(name, age)
        actual = p.get_greeting()
        expected = f'Hello! My name is {name} and Im {age} years old!'

        self.assertEqual(actual, expected)

    def test_invalid_name_shoud_raise_exception(self):
        name = None
        age = 1
        actual = lambda: Person(name, age)
        self.assertRaises(ValueError, actual)


if __name__ == '__main__':
    unittest.main()
