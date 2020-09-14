import unittest
from custom_list_package.custom_list import CustomList, CustomIndexException


class CustomList_RemoveTests(unittest.TestCase):
    def setup_list(self, *args):
        cl = CustomList()
        [cl.append(x) for x in args]
        return cl

    def test_customListRemove_whenIndexInMiddle_shouldRemoveIt(self):
        """"[1,2,3], remove at 1 index -> [1,3]"""
        cl = self.setup_list(1, 2, 3)
        result = cl.remove(1)

        self.assertEqual(2, result)

    def test_customListRemove_whenIndexIsZero_shouldRemoveIt(self):
        """"[1,2,3], remove at 0 index -> [2,3]"""
        cl = self.setup_list(1, 2, 3)
        result = cl.remove(0)

        self.assertEqual(1, result)

    def test_customListRemove_whenIndexIsLast_shouldRemoveIt(self):
        """"
        Last index is len(custom_list) - 1
        [1,2,3], remove at 2 index -> [1,2]
        """
        cl = self.setup_list(1, 2, 3)
        result = cl.remove(2)

        self.assertEqual(3, result)

    def test_customListRemove_whenListHasSingleElement_listShouldBeEmpty(self):
        """"[1], remove at 0 index -> []"""
        cl = self.setup_list(1)
        result = cl.remove(0)

        self.assertEqual(result, 1)
        self.assertListEqual([], cl.reverse())

    def test_customListRemove_whenIndexIsEqToLength_shouldRaiseException(self):
        """"
        [1,2,3,4], remove at len(custom_list) index -> IndexError
        """
        ll = [1,2,3,4]
        cl = self.setup_list(range(len(ll)))

        with self.assertRaises(CustomIndexException) as context:
            cl.remove(len(ll))

        self.assertIsNotNone(context.exception)

    def test_customListRemove_whenIndexIsLessThanZero_shouldRaiseException(self):
        """"
        [1,2,3,4], remove at -1 index -> IndexError
        """
        ll = [1,2,3,4]
        cl = self.setup_list(range(len(ll)))

        with self.assertRaises(CustomIndexException) as context:
            cl.remove(-1)

        self.assertIsNotNone(context.exception)



if __name__ == '__main__':
    unittest.main()
