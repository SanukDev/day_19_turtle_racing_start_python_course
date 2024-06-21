from turtle import Turtle, Screen
import random

tim = Turtle(shape="turtle")
jimi = Turtle(shape="turtle")
bili = Turtle(shape="turtle")
timo = Turtle(shape="turtle")
tomy = Turtle(shape="turtle")
screen = Screen()
list_object = [tim, jimi, bili, timo, tomy]
def init_turtle(object, x, y, color):
    object.color(color)
    object.penup()
    object.goto(x=x, y=y)

screen.setup(width=800, height=500)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color")
colors = ["red", "orange", "yellow", "blue", "green", "purple"]


init_turtle(tim, -380, -100, colors[0])
init_turtle(timo, -380, -50, colors[3])
init_turtle(jimi, -380, 0, colors[2])
init_turtle(bili, -380, 50, colors[1])
init_turtle(tomy, -380, 100, colors[4])

end_race = False
if user_bet:
    end_race = True

while end_race:
    for turtle_object in list_object:
        if turtle_object.xcor() > 370:
            end_race = False
            winning_color = turtle_object.pencolor()
            if winning_color == user_bet:
                print(f"You've won!! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost!! The {winning_color} turtle is the winner")
        rand_position = random.randint(1,10)
        turtle_object.forward(rand_position)

screen.exitonclick()