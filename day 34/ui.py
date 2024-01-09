from tkinter import ttk
import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.datadb = quiz_brain
        self.root = tk.Tk()
        self.root.title('Quizzler')
        self.root.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = tk.Label(text='Score: 0', fg='white', bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = tk.Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text='Some Question Text',
            fill=THEME_COLOR,
            font=('Arial', 20, 'italic')
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = tk.PhotoImage( file= r'100 days of code\day 34\images\true.png')
        False_img = tk.PhotoImage( file=r'100 days of code\day 34\images\false.png')

        self.true_button = tk.Button(
            image=true_img,
            highlightthickness=0, 
            background=THEME_COLOR,
            command=self.true_pressed
            )
        self.false_button = tk.Button(
            image=False_img, 
            highlightthickness=0, 
            background=THEME_COLOR,
            command=self.false_pressed
            )
        
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)
        
        self.get_next_question()
        
        self.root.mainloop()


    def get_next_question(self):
        self.canvas.config(bg='#ffffff')

        if self.datadb.still_has_questions():
            question = self.datadb.next_question()
            self.canvas.itemconfig(self.question_text, text=question)
        else:
            self.canvas.itemconfig(self.question_text, text='U\'ve reached the end of the quiz.')
            self.true_button.config(state='disable')
            self.false_button.config(state='disabled')
    def true_pressed(self):
        result = self.datadb.check_answer('True')
        self.give_feedback(result)
    def false_pressed(self):
        result = self.datadb.check_answer('False')
        self.give_feedback(result)

    def give_feedback(self, result):
        if result:
            self.canvas.config(background='#00ff00')
            self.score_label.config(text=f'Score: {self.datadb.score}')
        else:
            self.canvas.config(background='#ff0000')

        self.root.after(1000, self.get_next_question)

