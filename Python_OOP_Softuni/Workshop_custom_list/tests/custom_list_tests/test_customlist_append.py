import unittest
from custom_list_package.custom_list import CustomList


class Customlist_AppendTests(unittest.TestCase):

    def setup_list(self, *args):
        cl = CustomList()
        [cl.append(x) for x in args]
        return cl

    def test_customListAppend_whenEmptyList_shouldReturnListWithElement(self):
        value = 5

        cl = self.setup_list()
        result = cl.append(value)

        self.assertEqual([value], result)

    def test_customListAppend_whenListHasTwoElements_shouldReturnListWithNewElementAtEnd(self):
        cl = self.setup_list(1, 2, 3)
        result = cl.append(4)

        self.assertEqual([1, 2, 3, 4], result)


if __name__ == '__main__':
    unittest.main()
