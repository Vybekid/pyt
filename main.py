import colorsys
from turtle import *

# --- Setup the screen and turtle ---
bgcolor("black")
speed(0)
pensize(2)
hideturtle()

# --- Settings for the pattern ---
num_stars = 75     # How many stars to draw in the spiral
hue = 0.0          # The starting color

# --- Main drawing loop ---
for i in range(1, num_stars + 1):
    # Calculate the color for this star
    color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    pencolor(color)
    
    # 1. Draw one star
    begin_fill()  # Optional: to fill the stars with color
    for _ in range(5):
        forward(i * 4)  # The stars get bigger as 'i' increases
        right(144)      # The angle to make a 5-pointed star
    end_fill()    # Optional: finish filling the star
    
    # 2. Rotate the turtle to position for the next star
    right(360 / num_stars + 1)
    
    # 3. Advance to the next color
    hue += 1.0 / num_stars
    
done()