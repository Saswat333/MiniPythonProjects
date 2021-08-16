class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        current_text = current_question.question
        correct_ans = current_question.answer
        self.question_number += 1
        user_answer = input(f" Q.{self.question_number}: {current_text} (True/False): ")
        self.check_answer(user_answer, correct_ans)

    def check_answer(self, user_ans, actual_ans):
        if user_ans.lower() == actual_ans.lower():
            print("You are right !!")
            self.score += 1
        else:
            print("Wrong answer")
        print(f"The correct answer was: {actual_ans}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")
