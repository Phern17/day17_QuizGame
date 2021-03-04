class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def next_question(self):
        curr_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {curr_question.text} (True or False)?: ")
        self.check_answer(user_answer, curr_question.answer)

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            print("You're correct")
            self.score += 1
        else:
            print("You're wrong")
        print(f"The correct answer is {correct_ans}\nYour current score is: {self.score}/{self.question_number}\n")
