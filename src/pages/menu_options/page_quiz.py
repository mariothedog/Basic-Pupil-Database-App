import tkinter as tk
import json

from pages.frame_page import FramePage
import constants
import pages.menu_options.page_option_menu as page_option_menu


class PageQuiz(FramePage):
    def __init__(self, app, *args, **kwargs):
        super().__init__(app, *args, **kwargs)
        with open(constants.JSON_QUESTIONS, "a+") as file:
            file.seek(0)
            self.questions_data = json.load(file)

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

        label_question_num = tk.Label(
            frame_questions, text="Question 0", font=("TkDefaultFont", 12))
        label_question = tk.Label(frame_questions, text="Question", font=(
            "TkDefaultFont", 10), wraplength=150)
        label_question_num.grid()
        label_question.grid(row=1, column=0)

        label_points = tk.Label(
            frame_top, text="Points: 0", relief=tk.SUNKEN, borderwidth=1)
        label_points.grid(row=0, column=2)

        frame_answers = tk.Frame(self, relief=tk.RIDGE, borderwidth=1)
        frame_answers.grid(row=1, column=0, columnspan=2, sticky=tk.N)

        for letter in ("A", "B", "C", "D"):
            button_answer = tk.Button(frame_answers, width=2, text=letter)
            button_answer.grid()

        for i, letter in enumerate(("A", "B", "C", "D")):
            label_answer = tk.Label(frame_answers, text="Answer %s" % letter)
            label_answer.grid(row=i, column=1)

    def cancel(self):
        self.app.show_page(page_option_menu.PageOptionMenu)
