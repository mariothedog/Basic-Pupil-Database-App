import tkinter as tk

from pages.frame_page import FramePage
import pages.menu_options.page_option_menu as page_option_menu


class PageQuizOver(FramePage):
    def create_widgets(self):
        for i in range(2):
            self.rowconfigure(i, weight=1)
        self.columnconfigure(0, weight=1)

        frame_labels = tk.Frame(self)
        frame_labels.grid(sticky=tk.S)

        self.label_total_score = tk.Label(frame_labels)
        self.label_total_score.grid()

        self.label_message = tk.Label(frame_labels)
        self.label_message.grid()

        button_finish = tk.Button(self, text="Finish", command=self.finish)
        button_finish.grid(sticky=tk.N)
    
    def finish(self):
        self.app.show_page(page_option_menu.PageOptionMenu)
    
    def on_show(self, **kwargs):
        questions_data = kwargs["questions_data"]
        score = kwargs["score"]
        num_questions = len(questions_data)

        self.label_total_score.config(text="Total Score: %d/%d" % (score, num_questions))

        if score <= num_questions * 0.2:
            message = "Terrible!"
        elif score <= num_questions * 0.6:
            message = "You did okay"
        else:
            message = "Well done!"
        self.label_message.config(text=message)