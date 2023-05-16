import turtle
import time
import random
import threading

# Window definition
window = turtle.Screen()
window.screensize(400, 400)
window.bgcolor("Light Blue")
window.bgpic("bg.gif")
window.addshape("t4.gif")
window.addshape("t5.gif")
window.listen()

# Turtle definitions
turtle_1 = turtle.Turtle()
turtle_1.shapesize(3)
turtle_1.shape("t5.gif")
turtle_1.color("green")
turtle_1.penup()

countdown = turtle.Turtle()
countdown.hideturtle()
countdown.penup()

score_text = turtle.Turtle()
score_text.hideturtle()
score_text.penup()

# Settings
scr = 0
game_time: int = 30
elapsed_time = 0


def timer(seconds):
    print("timer started")
    turtle_1.shape("t4.gif")
    countdown.setpos(100, 225)
    score_text.setpos(160, 255)
    score_text.color("Red")
    score_text.write("Score: " + str(scr), font=("comic sans MS", 20, "bold"), align="left")
    mins = seconds // 60
    secs = seconds % 60
    while mins > 0 or secs > 0:
        countdown.clear()
        countdown.write("Countdown: " + str(mins).zfill(2) + ":" + str(secs).zfill(2),
                        font=("comic sans MS", 20, "bold"))
        secs -= 1
        if secs < 0:
            mins -= 1
            secs = 59
        time.sleep(1)
        if mins == 0 and secs <= 0:
            turtle_1.hideturtle()
            turtle_1.setpos(0, 0)
            countdown.clear()
            countdown.setpos(-300, 220)
            score_text.setpos(120, 220)
            turtle_1.shape("t5.gif")
            turtle_1.showturtle()
            for i in range(0, 53, 1):
                i += 1
                countdown.clear()
                countdown.write("Game over!", font=("comic sans MS", int(i / 2), "bold"), align="left")
                score_text.clear()
                score_text.write("Score: " + str(scr), font=("comic sans MS", int(i / 2), "bold"), align="left")
                turtle_1.speed(0)
                window.tracer(2)
                turtle_1.circle(i * 4+20, 10)


def turtle_run(mins, secs):
    global elapsed_time
    time.sleep(0.2)
    print("turtle_run started")
    start_time = time.time()
    while mins > 0 or secs > 0:

        if mins == 0 and secs == 0:
            turtle_1.hideturtle()

        elapsed_time = time.time() - start_time
        turtle_1.hideturtle()
        turtle_1.setpos(random.randint(-300, 300), random.randint(-250, 180))
        turtle_1.showturtle()
        time.sleep(0.6)
        if elapsed_time > game_time:
            break


def catch(x, y):
    print("catch started")
    turtle_1.onclick(score)


def score(x, y):
    global elapsed_time
    if turtle_1.isvisible() and turtle_1.distance(x, y) < 30 and elapsed_time < game_time:
        global scr
        scr += 1
        score_text.clear()
        score_text.write("Score: " + str(scr), font=("comic sans MS", 20, "bold"))
        turtle_1.shape("t5.gif")
        # window.tracer(1,70)
        time.sleep(0.25)
        turtle_1.shape("t4.gif")
        turtle_1.hideturtle()
        print("score working...")


def start_game(x, y):
    global elapsed_time
    print("Game started")
    score_text.clear()
    countdown.clear()
    countdown.color("Black")
    t1 = threading.Thread(target=timer, args=(game_time,))
    t2 = threading.Thread(target=turtle_run, args=(0, game_time))
    t1.start()
    print("t1 started")
    t2.start()
    print("t2 started")
    if turtle_1.isvisible() and turtle_1.distance(x, y) < 30 and elapsed_time < game_time:
        window.onclick(catch)


if __name__ == '__main__':
    score_text.setpos(-200, 225)
    score_text.color("Black")
    score_text.write("Catch the Turtle", align="left", font=("comic sans MS", 40, "bold"))
    countdown.setpos(-150, -290)
    countdown.color("Black")
    countdown.write("Click to start...", align="left", font=("comic sans MS", 40, "bold"))
    window.onclick(start_game)
    window.mainloop()
