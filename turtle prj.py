import time
import datetime as dt
import turtle

# create a turtle to display time
t = turtle.Turtle()

# create a turtle to create rectangle box
t1 = turtle.Turtle()

# create screen
s = turtle.Screen()

# function to change background color based on time
def change_background_color(hr):
    if 6 <= hr < 12:
        s.bgcolor("orange")  # morning
    elif 12 <= hr < 18:
        s.bgcolor("sky blue")  # afternoon
    else:
        s.bgcolor("dark blue")  # night

# obtain current hour, minute and second
# from the system
now = dt.datetime.now()
hr = now.hour
min = now.minute
sec = now.second

t1.pensize(3)
t1.color('black')
t1.penup()

# set the position of turtle
t1.goto(-20, 0)
t1.pendown()

# create rectangular box
for i in range(2):
    t1.forward(200)
    t1.left(90)
    t1.forward(70)
    t1.left(90)

# hide the turtle
t1.hideturtle()

change_background_color(hr)

while True:
    t.hideturtle()
    t.clear()
    # display the time
    now = dt.datetime.now()
    hr = now.hour
    min = now.minute
    sec = now.second
    
    if hr > 12:
        hr -= 12
        am_pm = "PM"
    else:
        am_pm = "AM"
        
    change_background_color(now.hour)
    
    t.write(f"{hr:02d}:{min:02d}:{sec:02d} {am_pm}",
            font=("Arial Narrow", 35, "bold"))
    time.sleep(1)