from project.reptile import Reptile


class Snake(Reptile):

    def __init__(self, name):
        Reptile.__init__(self, name)



# snake = Snake("Python")
# print(snake.get_name())