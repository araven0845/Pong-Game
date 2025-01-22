from turtle import Turtle

class Scoreboard(Turtle):
    """
    Scoreboard class inherits from Turtle and handles displaying and updating the scores.
    """

    def __init__(self):
        """
        Initialize the scoreboard with initial scores and display them at the top of the screen.
        """
        super().__init__()
        self.r_score = 0  # Score for the right player
        self.l_score = 0  # Score for the left player
        self.penup()  # Disable drawing
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Clear the screen and redraw the current scores for both players.
        """
        self.clear()
        # Display left player's score
        self.goto(-150, 330)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        # Display right player's score
        self.goto(150, 330)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        """
        Increment the left player's score by 1 and update the scoreboard.
        """
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """
        Increment the right player's score by 1 and update the scoreboard.
        """
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self):
        """
        Display a "Game Over" message at the center of the screen.
        """
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 24, "normal"))
