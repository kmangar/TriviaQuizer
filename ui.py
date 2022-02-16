from tkinter import *

THEME_COLOR = "#375362"
SCORE = 0


class QuizInterface:

    def __init__(self):
        self.window = Tk()

        self.window.title("TRIVIA QUIZZER")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text=f"Score: {SCORE}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white" ,highlightthickness=0, )
        self.quiz_ques = self.canvas.create_text(150, 125, text="Empty text", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)


        self.true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_img, highlightthickness=0)
        self.true_button.grid(row=2, column=0)

        self.false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_img, highlightthickness=0)
        self.false_button.grid(row=2, column=1)

        self.window.mainloop()
