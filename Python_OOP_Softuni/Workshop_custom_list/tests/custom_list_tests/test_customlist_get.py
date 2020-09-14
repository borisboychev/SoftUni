import unittest
from custom_list_package.custom_list import CustomList, CustomIndexException, CustomTypeException

class CustomList_GetTest(unittest.TestCase):
    def setup_list(self, *args):
        cl = CustomList()
        [cl.append(x) for x in args]
        return cl

    def test_customListGet_whenIndexInMiddle_shouldReturnIt(self):
        """"[1,2,3], get at 1 index -> 2"""
        cl = self.setup_list(1, 2, 3)
        result = cl.get(1)

        self.assertEqual(2, result)

    def test_customListGet_whenIndexIsZero_shouldReturnIt(self):
        """"[1,2,3], get at 0 index -> 1"""
        cl = self.setup_list(1, 2, 3)
        result = cl.get(0)

        self.assertEqual(1, result)

    def test_customListGet_whenIndexIsLast_shouldReturnIt(self):
        """"
        Last index is len(custom_list) - 1
        [1,2,3], get at 2 index -> 3
        """
        cl = self.setup_list(1, 2, 3)
        result = cl.get(2)

        self.assertEqual(3, result)

    def test_customListGet_whenListHasSingleElement_shouldReturnIt(self):
        """"[1], get at 0 index -> 1"""
        cl = self.setup_list(1)
        result = cl.remove(0)

        self.assertEqual(result, 1)

    def test_customListGet_whenIndexIsEqToLength_shouldRaiseException(self):
        """"
        [1,2,3,4], get at len(custom_list) index -> IndexError
        """
        ll = [1,2,3,4]
        cl = self.setup_list(range(len(ll)))

        with self.assertRaises(CustomIndexException) as context:
            cl.get(len(ll))

        self.assertIsNotNone(context.exception)

    def test_customListGet_whenIndexIsLessThanZero_shouldRaiseException(self):
        """"
        [1,2,3,4], get at -1 index -> IndexError
        """
        ll = [1,2,3,4]
        cl = self.setup_list(range(len(ll)))

        with self.assertRaises(CustomIndexException) as context:
            cl.get(-1)

    def test_customListGet_whenIndexIsNotInt_shouldRaiseException(self):
        cl = self.setup_list(1,2,3)

        with self.assertRaises(CustomTypeException) as context:
            cl.get('a')


if __name__ == '__main__':
    unittest.main()
