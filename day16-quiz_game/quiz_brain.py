class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.questions_list = q_list

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_input = input(f"Q.{self.question_number}: {current_question.text} (TRUE/FALSE)?: ")
        self.check_answer(user_input, current_question.answer)

    def still_has_questions(self):
        # if self.question_number <= len(self.questions_list):
        #     return True
        # else:
        #     return False
        # or can be done with
        return self.question_number < len(self.questions_list)

    def check_answer(self, user_input, correct_answer):
        if user_input.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right")
        else:
            print("You got it wrong")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")