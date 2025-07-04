import colorsys
from turtle import *

# --- Setup the screen and turtle ---
bgcolor("black")
speed(0)          # Use the fastest drawing speed
pensize(2)        # A slightly thicker line looks good
hideturtle()

# --- Settings for the pattern ---
num_circles = 36  # The number of circles to draw
radius = 150      # The radius of each circle
hue = 0.0         # Starting hue for the color cycle

# --- Main drawing loop ---
for _ in range(num_circles):
    # Calculate a color from the rainbow spectrum
    color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    pencolor(color)
    
    # 1. Draw a complete circle
    circle(radius)
    
    # 2. Rotate the turtle for the next circle
    left(360 / num_circles)
    
    # 3. Advance the hue to get the next color in the rainbow
    hue += 1.0 / num_circles

done() # Keep the window open