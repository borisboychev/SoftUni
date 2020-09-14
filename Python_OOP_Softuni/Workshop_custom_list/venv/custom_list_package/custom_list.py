from typing import List
from custom_list_package.exceptions import CustomValueError, CustomIndexException, CustomTypeException, CustomBoundException, CustomListSumException
from collections import Iterable


class CustomList:
    def __init__(self, *args):
        self.sequence = [x for x in args]

    def validate_int(self, index):
        if not isinstance(index, int):
            raise CustomTypeException(
                f'CustomList: argument does not support that type it must be an int it was {type(index)}')

    def append(self, value) -> List:
        self.sequence += [value]
        return self.sequence

    def remove(self, index):
        if index < 0:
            raise CustomIndexException('CustomList: index out of range')
        try:
            val_to_remove = self.sequence[index]
            del self.sequence[index]
            return val_to_remove
        except IndexError as ex:
            raise CustomIndexException('CustomList: index out of range')
        except TypeError as ex:
            CustomTypeException(
                f'CustomList: argument does not support that type it must be an int it was {type(index)}')

    def get(self, index):
        self.validate_int(index)
        if index < 0:
            raise CustomIndexException('CustomList: index out of range')
        try:
            el_to_get = self.sequence[index]
            return el_to_get
        except IndexError as ex:
            raise CustomIndexException('CustomList: index out of range')
        except TypeError as ex:
            raise CustomTypeException('Index type must be an int')

    def extend(self, iterable):
        if isinstance(iterable, Iterable):
            self.sequence += list(iterable)
            return self.sequence
        raise CustomTypeException('CustomList: argument must be iterable to extend')

    def insert(self, index, value):
        self.validate_int(index)
        try:
            sliced = self.sequence[index:]
            self.sequence = self.sequence[0:index]
            self.sequence += [value]
            self.sequence += sliced
            return self.sequence
        except IndexError as ex:
            raise CustomIndexException('CustomList: index out of range')

    def pop(self):
        try:
            popped_value = self.sequence[-1]
            del self.sequence[-1]
        except IndexError as ex:
            raise CustomIndexException('CustomList: no elements to pop')

        return popped_value

    def clear(self):
        self.sequence = []
        return self.sequence

    def index(self, value):
        value_on_index = [x for x in range(len(self.sequence)) if value == self.sequence[x]]
        if value_on_index:
            return value_on_index[0]
        raise CustomValueError('CustomList: No such value in CustomList')

    def count(self, value):
        value_counter = [x for x in self.sequence if x == value]
        if value_counter:
            return len(value_counter)
        raise CustomValueError('CustomList: such values does not exist')

    def reverse(self):
        return self.sequence[::-1]

    def copy(self):
        list_copy = CustomList(*[x for x in self.sequence])
        return list_copy

    def size(self):
        return len(self.sequence)

    def add_first(self, value):
        self.sequence = [value] + self.sequence

    def dictionarize(self):
        dictionarized_list = {}
        for i in range(self.size()):
            if i % 2 == 0:
                if i + 1 < len(self.sequence):
                    dictionarized_list[self.sequence[i]] = self.sequence[i + 1]
                    continue
                dictionarized_list[self.sequence[i]] = ' '

        return dictionarized_list

    def move(self, amount):
        if len(self.sequence) == 0:
            return self.sequence
        self.sequence = self.sequence[amount:] + self.sequence[:amount]
        return self.sequence

    def sum(self):
        summed_elements = 0
        for el in self.sequence:
            if isinstance(el, int) or isinstance(el, float):
                summed_elements += el
                continue
            try:
                summed_elements += len(el)
            except TypeError as ex:
                raise CustomListSumException("CustomList: provide a len method to custom object")

        return summed_elements

    def overbound(self):
        max_number = float('-inf')
        element = None
        for i in range(len(self.sequence)):
            if isinstance(self.sequence[i], int) or isinstance(self.sequence[i], float):
                if max_number < self.sequence[i]:
                    max_number = self.sequence[i]
                    element = self.sequence[i]
                    continue
                continue
            try:
                size_of_el = len(self.sequence[i])
                if size_of_el > max_number:
                    max_number = size_of_el
                    element = self.sequence[i]
            except TypeError as ex:
                raise CustomBoundException('CustomList: provide a len method to custom object')

        return self.index(element)

    def underbound(self):
        min_number = float('inf')
        element = None
        for i in range(len(self.sequence)):
            if isinstance(self.sequence[i], int) or isinstance(self.sequence[i], float):
                if min_number > self.sequence[i]:
                    min_number = self.sequence[i]
                    element = self.sequence[i]
                    continue
                continue
            try:
                size_of_el = len(self.sequence[i])
                if size_of_el < min_number:
                    min_number = size_of_el
                    element = self.sequence[i]
            except TypeError as ex:
                raise CustomBoundException('CustomList: provide a len method to custom object')

        return self.index(element)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"[{', '.join(str(x) for x in self.sequence)}]"


# my_list = [1, 2]                     4
my_custom_list = CustomList(1, 2, 3, 'abcd')
# my_custom_list.append(4)
# print(my_custom_list)
# my_custom_list.remove(1)
# print(my_custom_list)
# print(my_custom_list.get(2))
# my_custom_list.extend([1, 2, 3])
# print(my_custom_list)
# my_custom_list.insert(1, 'abv')
# print(my_custom_list)
# print(my_custom_list.index(3))
# print(my_custom_list.count(3))
# print(my_custom_list.reverse())
#
# print(my_custom_list.dictionarize())
# # print(my_custom_list.move(2))
# print(my_custom_list.sum())
# print(my_custom_list.overbound())
# print(my_custom_list.underbound())
