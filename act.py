from dataclasses import dataclass

from utils import glitch_text, clear_screen


@dataclass
class Question:
    question_number: int
    question: str
    answers: list

    def __str__(self):
        return f"Вопрос №{self.question_number}: {self.question}"


@dataclass
class SecretQuestion(Question):
    def __str__(self):
        return f"Вопрос №{self.question_number}: {glitch_text(self.question)}"


class Act:
    """
    Act class.
    :number: int - Act number.
    :questions_count: int - Questions count in a current act.
    :questions_list: list[Question] - List with all questions for a current act.
    """
    def __init__(self, number: int, questions_count: int, questions_list: list[Question]):
        self.number = number
        self.questions_count = questions_count
        self.questions_list = questions_list
        self.user_answers = []

        if len(self.questions_list) != self.questions_count:
            print("WARNING: Количество переданных вопросов не соответствует количеству вопросов")

    def act_start(self):
        print(f"Приветствуем вас на акте №{self.number}!\nВсего будет {self.questions_count} вопросов!")

        is_ready = int(input("1-готов;0-не готов > "))
        while is_ready != 0 or is_ready != 1:
            is_ready = int(input("1-готов;0-не готов > "))

        if is_ready:
            clear_screen()
            for question in self.questions_list:
                clear_screen()
                print("-" * 10)
                print(question)
                print("-" * 10)

                for answer_number, answer in enumerate(question.answers, start=1):
                    print(answer_number, ".", answer, sep="")

                user_choose = int(input("> "))
                self.user_answers.append((question.question_number, user_choose))