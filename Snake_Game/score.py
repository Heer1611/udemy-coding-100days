from turtle import Turtle

ALIGNMENT = "center"
FONT = ("arial", 22,"normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_score()
        
    def update_score(self):
            self.write(f"Score: {self.score}", align= ALIGNMENT, font= FONT)
    
    def end_game(self):
        self.goto(0,0)
        self.write("Game Over" ,align= ALIGNMENT, font= FONT)
    
    def increase_score(self):
        self.score +=1
        self.write(f"Score: {self.score}", align= ALIGNMENT, font= FONT)
        self.clear()
        self.update_score()
        
