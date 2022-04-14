from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt") as file:
            content = file.read()
        self.score = 0
        self.high_score = int(content)
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.updatescore()
        self.hideturtle()


    def updatescore(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGNMENT,
                   font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.updatescore()


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT,font=FONT)

    def increase_score(self):
        self.score += 1
        self.updatescore()



