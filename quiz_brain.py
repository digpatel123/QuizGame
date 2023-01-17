class QuizBrain:

    def __init__(self, q_list):
        self.q_list = q_list
        self.q_num = 0

    def next_question(self, que, ans):
        current_que = self.q_list[self.q_num]
        self.q_num += 1
        return input(f"Q.{self.q_num}: {current_que.text} (True/False): ")

