from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
SCORE = 0


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("TRIVIA QUIZZER")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text=f"Score: {SCORE}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0, bd=0)
        self.quiz_ques = self.canvas.create_text(150, 125,
                                                 text="Empty text",
                                                 width=280,
                                                 fill=THEME_COLOR,
                                                 font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        self.true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(
            image=self.true_img,
            highlightthickness=0,
            command=self.true_pressed,
            bd=0)
        self.true_button.grid(row=2, column=0)

        self.false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(
            image=self.false_img,
            highlightthickness=0,
            command=self.false_pressed,
            bd=0)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_ques, text=q_text)
            self.buttons_state("active")
        else:
            self.canvas.itemconfig(self.quiz_ques, text="You have Finished the Quiz")
            self.buttons_state("disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        self.buttons_state("disabled")

        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question )
        # self.score_label.config(text=f"Score: {self.quiz.score}")


    def buttons_state(self, state: str):
        self.true_button.config(state=state)
        self.false_button.config(state=state)