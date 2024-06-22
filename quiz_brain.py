class QuizBrain:
    def __init__(self, q_list):
        self.question_num = 0
        self.question_list = q_list
        self.user_score = 0
        
    def Still_has_q (self):
        return self.question_num < len(self.question_list)
           
            
    
    
    def next_q(self):
        current_q = self.question_list[self.question_num]
        self.question_num += 1
        user_ans = input(f"Q.{self.question_num}: {current_q.text} (True/False): ")
        self.check_ans(user_ans, current_q.answer)
        
    def check_ans(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            print("You got it right")
            self.user_score += 1
    
        else:
            print("That's wrong")
        print(f"The correct answer was: {correct_ans}.")
        print(f"Your current score is {self.user_score}/{self.question_num}")