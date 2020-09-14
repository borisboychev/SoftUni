from triangle.print_line import *


def print_triangle(n):
    [print_line(1, x) for x in range(n)]
    [print_line(1, x) for x in range(n , 0 , -1)]

