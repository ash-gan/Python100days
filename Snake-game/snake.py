from turtle import Turtle
SNAKE_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
DIRECTIONS = {'up': 90, 'right': 0, 'left': 180, 'down': 270}


class Snake:

    def __init__(self):
        self.segments = []
        self.create_segments()
        self.head = self.segments[0]

    def create_segments(self):
        for position in SNAKE_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_object = Turtle("square")
        new_object.color("white")
        new_object.penup()
        new_object.speed("slowest")
        new_object.goto(position)
        self.segments.append(new_object)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DIRECTIONS['down']:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != DIRECTIONS['up']:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != DIRECTIONS['right']:
            self.head.setheading(180)

    def right(self):
        if self.segments[0].heading() != DIRECTIONS['left']:
            self.head.setheading(0)

    def reset_snake(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_segments()
        self.head = self.segments[0]

