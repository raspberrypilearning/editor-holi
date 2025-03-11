from p5 import *
from burst import *

num_circles=5  # Number of circles
min_radius=2  # Smallest circle size
max_radius=8  # Largest circle size

def mouse_pressed():
    create_burst(mouse_x, mouse_y, 
    num_circles, min_radius, max_radius)

run()
