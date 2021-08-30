from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
FONT = ("Courier", 16, "normal")


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)
        self.cross_finish_line = False

    def move_turtle(self):
        self.cross_finish_line = False
        if self.ycor() >= FINISH_LINE_Y:
            self.cross_finish_line = True
            self.finish_level()
        else:
            self.forward(MOVE_DISTANCE)

    def finish_level(self):
        self.goto(STARTING_POSITION)
