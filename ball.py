from turtle import Turtle

# Starting position of the ball
START_POS = (0, 0)


class Ball(Turtle):
    """
    Ball class inherits from Turtle and represents the ball in the Pong game.
    """

    def __init__(self):
        """
        Initialize the ball with default settings, such as position, shape, size, and movement direction.
        """
        super().__init__()
        self.shape("circle")
        self.penup()  # Disable drawing
        self.goto(START_POS)  # Start at the center of the screen
        self.shapesize(stretch_wid=1.5, stretch_len=1.5)  # Resize the ball
        self.color("white")
        self.x_move = 2  # Horizontal movement speed
        self.y_move = 2  # Vertical movement speed

    def move(self):
        """
        Move the ball to a new position based on its current movement direction.
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """
        Reverse the ball's vertical direction when it hits the top or bottom wall.
        """
        self.y_move *= -1

    def bounce_x(self):
        """
        Reverse the ball's horizontal direction when it hits a paddle and increase its speed slightly.
        """
        self.x_move *= -1
        self.speed_up()

    def speed_up(self):
        """
        Gradually increase the ball's speed after hitting a paddle.
        """
        # Adjust horizontal speed
        if self.x_move < 0:
            self.x_move -= 0.25
        else:
            self.x_move += 0.25

        # Adjust vertical speed
        if self.y_move < 0:
            self.y_move -= 0.25
        else:
            self.y_move += 0.25

    def reset(self):
        """
        Reset the ball to the starting position and restore its initial speed.
        Also reverses the horizontal direction to switch turns.
        """
        self.goto(START_POS)

        # Reset movement speed to initial values
        self.x_move = -2 if self.x_move < 0 else 2
        self.y_move = -2 if self.y_move < 0 else 2

        self.bounce_x()  # Change direction to give the other player a chance
