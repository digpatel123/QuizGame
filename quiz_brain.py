class QuizBrain:

    def __init__(self, q_list):
        self.q_list = q_list
        self.q_num = 0
        self.score = 0

    def next_question(self):
        current_que = self.q_list[self.q_num]
        self.q_num += 1
        user_ans = input(f"Q.{self.q_num}: {current_que.text} (True/False): ")
        self.check_ans(user_ans, current_que.answer)

    def still_has_question(self):
        return self.q_num < len(self.q_list)

    def check_ans(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("You are correct!")
            self.score += 1

        else:
            print("You are wrong.")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is {self.score}/{self.q_num} \n")

