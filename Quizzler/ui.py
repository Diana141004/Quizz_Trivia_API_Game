from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"
FONT = ("Arial", 20,"italic")

class QuizzInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg = THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(width = 300, height = 250, bg = "white", highlightthickness=0)

        self.text_canvas = self.canvas.create_text(150, 125, text="text for test", font = FONT, fill = "black", width = 280)
        self.canvas.grid(column = 0, columnspan=2, row = 1, pady=(30,30))

        right_image = PhotoImage(file = "images/true.png")
        wrong_image = PhotoImage(file = "images/false.png")

        self.right_button = Button(image= right_image,highlightthickness=0,padx = 20, pady = 20, command = self.right_check)
        self.right_button.grid(column=0, row = 2)

        self.wrong_button = Button(image = wrong_image,highlightthickness=0,padx = 20, pady = 20, command= self.false_check)
        self.wrong_button.grid(column = 1, row = 2)

        self.score_label = Label(text = "Score: 0",  font = FONT, highlightthickness=0, bg = THEME_COLOR, padx = 20, pady = 20, fg = "white")
        self.score_label.grid(column = 1, row = 0)

        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text_canvas, text = q_text)
            self.score_label.config(text =f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.text_canvas, text = "You've reached the end of the quiz!")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def false_check(self):
        self.get_feedback( self.quiz.check_answer("False"))


    def right_check(self):
        self.get_feedback( self.quiz.check_answer("True"))


    def get_feedback(self,answ):
        if answ:
            self.canvas.configure(bg = "green")
            self.window.after(1000,self.get_next_question)
        else:
            self.canvas.configure(bg = "red")
            self.window.after(1000,self.get_next_question)



