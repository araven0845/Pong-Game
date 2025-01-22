from turtle import Turtle

class Paddle(Turtle):
    """
    Paddle class inherits from Turtle and represents a paddle in the Pong game.
    """

    def __init__(self, pos):
        """
        Initialize the paddle at the specified position.
        """
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()  # Disable drawing
        self.shapesize(stretch_wid=7.5, stretch_len=1.5)  # Resize paddle
        self.goto(pos)  # Place paddle at the given position

    def up(self):
        """
        Move the paddle up by 30 units if within the screen boundary.
        """
        if self.ycor() < 375:  # Upper boundary limit
            self.goto(self.xcor(), self.ycor() + 30)

    def down(self):
        """
        Move the paddle down by 30 units if within the screen boundary.
        """
        if self.ycor() > -375:  # Lower boundary limit
            self.goto(self.xcor(), self.ycor() - 30)
