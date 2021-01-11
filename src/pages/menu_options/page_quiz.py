import tkinter as tk
import json

from pages.frame_page import FramePage
import constants
import pages.menu_options.page_option_menu as page_option_menu


class PageQuiz(FramePage):
    def create_widgets(self):
        for i in range(2):
            self.rowconfigure(i, weight=1)
        self.columnconfigure(1, weight=1)

        frame_top = tk.Frame(self)
        frame_top.grid(columnspan=3, pady=(0, 20), sticky=tk.S)

        cancel_button = tk.Button(
            frame_top, text="Cancel", command=self.cancel)
        cancel_button.grid(sticky=tk.E)

        frame_questions = tk.Frame(frame_top)
        frame_questions.grid(row=0, column=1, padx=30)

        self.label_question_num = tk.Label(frame_questions, font=("TkDefaultFont", 12))
        self.label_question = tk.Label(frame_questions, font=("TkDefaultFont", 10), wraplength=150)
        self.label_question_num.grid()
        self.label_question.grid(row=1, column=0)

        self.label_score = tk.Label(
            frame_top, text="Score: 0", relief=tk.SUNKEN, borderwidth=1)
        self.label_score.grid(row=0, column=2)

        self.frame_answers = tk.Frame(self, relief=tk.RIDGE, borderwidth=1)
        self.frame_answers.grid(row=1, column=0, columnspan=2, sticky=tk.N)

        self.button_answers = []
        self.label_answers = []
    
    def on_show(self):
        self.setup_quiz()

    def cancel(self):
        self.app.show_page(page_option_menu.PageOptionMenu)
    
    def setup_quiz(self):
        with open(constants.JSON_QUESTIONS, "a+") as file:
            file.seek(0)
            self.questions_data = json.load(file)
        self.question_index = 0
        self.score = 0
        self.start_next_question()
    
    def end_quiz(self): # TODO
        print("Quiz ended!")

    def start_next_question(self):
        question_data = self.questions_data[self.question_index]
        question = question_data["question"]
        answers = question_data["answers"]
        num_answers = len(answers)

        question_num_formatted = "Question %d" % (self.question_index + 1)
        self.label_question_num.config(text=question_num_formatted)
        self.label_question.config(text=question)

        self.label_score.config(text="Score: %d" % self.score)

        for button in self.button_answers:
            button.grid_forget()
        for label in self.label_answers:
            label.grid_forget()
        
        self.button_answers = []
        self.label_answers = []

        for i in range(num_answers):
            letter = chr(65 + i)
            button = tk.Button(self.frame_answers, width=2, text=letter, command=lambda i=i: self.answer_question(question_data, i))
            label = tk.Label(self.frame_answers, text=answers[i])
            button.grid()
            label.grid(row=i, column=1, padx=5)
            self.button_answers.append(button)
            self.label_answers.append(label)
    
    def answer_question(self, question_data, answer_index):
        if answer_index == question_data["correct_answer_index"]:
            self.score += 1

        num_questions = len(self.questions_data)
        if self.question_index >= num_questions - 1:
            self.end_quiz()
        else:
            self.question_index += 1
            self.start_next_question()
