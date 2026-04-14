from p5 import *
from burst import *

num_circles = 15
min_radius = 6
max_radius = 18


def mouse_pressed():
    create_burst(mouse_x, mouse_y, num_circles, min_radius, max_radius)


run()
