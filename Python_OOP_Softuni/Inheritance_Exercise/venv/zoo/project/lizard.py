from project.reptile import Reptile


class Lizard(Reptile):

    def __init__(self, name):
        Reptile.__init__(self, name)

# lizard = Lizard("Gekko")
# print(lizard.get_name())