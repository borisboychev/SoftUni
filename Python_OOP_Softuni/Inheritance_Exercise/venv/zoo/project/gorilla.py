from project.mammal import Mammal


class Gorilla(Mammal):

    def __init__(self, name):
        Mammal.__init__(self, name)

#
# gorilla = Gorilla("Arnie")
# print(gorilla.get_name())