from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 14, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open("data.txt", "r") as data:
            self.high_score = int(data.read())
        self.score = 0
        self.penup()
        self.color("white")
        self.setposition(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.update_scoreboard()


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(str(self.score))
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.setposition(0, 0)
    #     self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)
