from p5 import *
import random

WIDTH, HEIGHT = 480, 320

def setup():
    size(WIDTH, HEIGHT)
    background(0)
    
def create_burst(x, y, num_circles=50, min_radius=2, max_radius=8):
    """Generates a burst effect at (x, y) with the given parameters."""
    for _ in range(num_circles):
        colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        radius = random.randint(min_radius, max_radius)
        dx = random.randint(-20, 20)
        dy = random.randint(-20, 20)
        fill(*colour)
        no_stroke()
        ellipse(x + dx, y + dy, radius, radius)
