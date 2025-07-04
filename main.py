import random
from turtle import *

# --- Setup the screen and turtle ---
bgcolor("black")
pencolor("green")   # The tree will be green
speed(0)
hideturtle()

# Position the turtle to start at the bottom
left(90)
penup()
backward(250)
pendown()

# --- The recursive function that draws the tree ---
def draw_branch(branch_length):
    if branch_length > 10:  # The condition to stop the recursion
        # 1. Draw the main branch
        forward(branch_length)

        # 2. Save the current position and heading
        position_stack.append(pos())
        heading_stack.append(heading())
        
        # 3. Turn and draw the right sub-branch (recursively)
        right(random.randint(15, 30))
        draw_branch(branch_length * random.uniform(0.6, 0.9))
        
        # 4. Restore position and draw the left sub-branch
        penup()
        setpos(position_stack.pop())
        setheading(heading_stack.pop())
        pendown()
        left(random.randint(15, 30))
        draw_branch(branch_length * random.uniform(0.6, 0.9))

# --- Start the drawing process ---
position_stack = []
heading_stack = []
draw_branch(100)
done()