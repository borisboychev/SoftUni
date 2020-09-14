from random import choice


class RandomList(list):

    def get_random_element(self):
        random_el = choice(self)
        self.remove(random_el)
        return random_el


""""Test Code"""
ll = RandomList([1, 2, 3, 4])
print(ll.get_random_element())
ll.append(5)
ll.pop()
