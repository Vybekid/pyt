import turtle
import time

def draw_environment(x_offset, y_offset, ground_y):
    t.pencolor("gray")
    t.penup()
    t.goto(x_offset - 250, y_offset + 100)
    t.dot(40)
    t.pencolor("white")
    t.goto(x_offset - 200, ground_y)
    t.pendown()
    t.goto(x_offset + 200, ground_y)

def draw_muzzle_flash(x, y):
    t.penup()
    t.goto(x, y)
    t.pencolor("yellow")
    t.pensize(2)
    t.pendown()
    for _ in range(6):
        t.forward(15)
        t.backward(15)
        t.right(60)

def draw_gun(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x + 30, y)
    t.goto(x + 30, y - 5)
    t.goto(x + 5, y - 5)
    t.goto(x, y)

def draw_stickman(
    x, y, color,
    pose="stand", angle=0
):
    t.setheading(0)
    t.pencolor(color)
    t.pensize(5)
    if pose == "dead":
        t.penup()
        t.goto(x - 30, y)
        t.pendown()
        t.forward(100)
        t.dot(30)
        t.backward(50)
        t.left(45)
        t.forward(40)
        t.backward(40)
        t.right(90)
        t.forward(40)
        return
    body_top_y = y + 100
    if pose == "hit":
        body_top_y -= 20
        t.setheading(angle)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x, body_top_y)
    t.dot(30)
    t.goto(x, body_top_y - 20)
    if pose == "stand":
        t.goto(x - 30, body_top_y - 40)
        t.penup()
        t.goto(x, body_top_y - 20)
        t.pendown()
        t.goto(x + 30, body_top_y - 40)
    elif pose == "aim_gun":
        draw_gun(x + 5, body_top_y - 25)
        t.penup()
        t.goto(x, body_top_y - 20)
        t.pendown()
        t.goto(x - 20, body_top_y - 40)
    elif pose == "scared" or pose == "hit":
        t.goto(x - 30, body_top_y + 10)
        t.penup()
        t.goto(x, body_top_y - 20)
        t.pendown()
        t.goto(x + 30, body_top_y + 10)
    t.setheading(0)
    t.penup()
    t.goto(x, y + 50)
    t.pendown()
    t.goto(x - 20, y)
    t.penup()
    t.goto(x, y + 50)
    t.pendown()
    t.goto(x + 20, y)

def draw_scene(
    p1_pos, p2_pos, p1_pose, p2_pose,
    bullet_pos=None, flash=False, hit_angle=0
):
    t.clear()
    draw_environment(X_OFFSET, Y_OFFSET, GROUND_Y)
    draw_stickman(
        p1_pos[0], p1_pos[1], "deepskyblue", p1_pose
    )
    draw_stickman(
        p2_pos[0], p2_pos[1], "red", p2_pose, angle=hit_angle
    )
    if flash:
        draw_muzzle_flash(p1_pos[0] + 35, GROUND_Y + 75)
    if bullet_pos:
        t.penup()
        t.goto(bullet_pos)
        t.pencolor("yellow")
        t.dot(8)
    screen.update()

def main():
    time.sleep(4)
    p1 = [P1_X, GROUND_Y]
    p2 = [P2_X, GROUND_Y]
    draw_scene(p1, p2, "stand", "stand")
    time.sleep(1)
    p1[0] += 15
    draw_scene(p1, p2, "stand", "stand")
    time.sleep(0.5)
    draw_scene(p1, p2, "aim_gun", "scared")
    time.sleep(0.5)
    p1[0] -= 10
    draw_scene(
        p1, p2, "aim_gun", "scared", flash=True
    )
    time.sleep(0.05)
    for i in range(1, 11):
        bullet_x = (p1[0] + 35 +
                    (i * (p2[0] - p1[0] - 35) / 10))
        draw_scene(
            p1, p2, "aim_gun", "scared",
            bullet_pos=(bullet_x, GROUND_Y + 70)
        )
        time.sleep(0.01)
    t.penup()
    t.goto(p2[0] - 10, GROUND_Y + 150)
    t.pencolor("orange")
    t.write("POW!", font=("Arial", 24, "bold"))
    for i in range(10):
        p2[1] -= 5
        draw_scene(
            p1, p2, "aim_gun", "hit", hit_angle=i * 5
        )
        time.sleep(0.03)
    time.sleep(0.5)
    draw_scene(p1, p2, "aim_gun", "dead")
    time.sleep(2)
    t.pencolor("gold")
    t.penup()
    t.goto(X_OFFSET, Y_OFFSET + 50)
    t.write(
        "Please Subscribe",
        align="center",
        font=("Arial", 36, "bold")
    )
    screen.update()

if __name__ == "__main__":
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Stickman Duel Animation")
    screen.tracer(0)
    t = turtle.Turtle()
    t.hideturtle()
    X_OFFSET = -200
    Y_OFFSET = 150
    P1_X = -100 + X_OFFSET
    P2_X = 100 + X_OFFSET
    GROUND_Y = -150 + Y_OFFSET
    main()
    turtle.done()