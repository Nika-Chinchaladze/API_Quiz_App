from tkinter import *
from PIL import Image, ImageTk
from Questions import ImportQuestion
from random import choice
from html import unescape

DF = ImportQuestion()


class QuizApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Quiz App")
        self.window.geometry("400x550")
        self.window.configure(bg="gray")
        # questions:
        self.data = DF.import_questions()
        self.score_counter = 0
        self.question_counter = 0
        self.answer = ""

        # score:
        self.score_label = Label(self.window, text=f"Score: {self.score_counter}", font=("Arial", 14, "bold"),
                                 bg="gray", fg="white smoke")
        self.score_label.place(x=305, y=15, width=90, height=30)

        # screen:
        self.main_frame = Frame(self.window, bg="gray")
        self.main_frame.place(x=0, y=50, width=400, height=350)

        self.question_label = Label(self.main_frame, fg="teal", text="", font=("Arial", 20, "italic"), wraplength=300)
        self.question_label.place(x=10, y=10, width=380, height=330)

        # buttons:
        true_image = Image.open("./img/true.png")
        true_photo = ImageTk.PhotoImage(true_image)
        self.true_button = Button(self.window, image=true_photo, bd=0, highlightthickness=0, command=self.check_true)
        self.true_button.image = true_photo
        self.true_button.place(x=20, y=410)

        false_image = Image.open("./img/false.png")
        false_photo = ImageTk.PhotoImage(false_image)
        self.false_button = Button(self.window, image=false_photo, bd=0, highlightthickness=0, command=self.check_false)
        self.false_button.image = false_photo
        self.false_button.place(x=280, y=410)

        # generate first question:
        self.generate_question()

    # ================================== FUNCTIONALITY ================================== #
    def generate_question(self):
        try:
            self.question_counter += 1
            result = choice(self.data)
            question = unescape(result["question"])
            self.answer = result["correct_answer"]
            self.question_label.config(text=f"Q.{self.question_counter}: {question}", bg="white", fg="teal")
            self.data.remove(result)
        except IndexError:
            self.question_label.config(text=f"Quiz Over! \nFinal Score: {self.score_counter}/10", justify="center",
                                       bg="pale green", fg="black")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_true(self):
        if self.answer == "True":
            self.question_label.config(bg="lime green", fg="white smoke")
            self.score_counter += 1
            self.score_label.config(text=f"Score: {self.score_counter}")
        else:
            self.question_label.config(bg="#FC5438", fg="white smoke")
        self.answer = ""
        self.window.after(2000, self.generate_question)

    def check_false(self):
        if self.answer == "False":
            self.question_label.config(bg="lime green", fg="white smoke")
            self.score_counter += 1
            self.score_label.config(text=f"Score: {self.score_counter}")
        else:
            self.question_label.config(bg="#FC5438", fg="white smoke")
        self.answer = ""
        self.window.after(2000, self.generate_question)


def launch_program():
    app = Tk()
    QuizApp(app)
    app.mainloop()


if __name__ == "__main__":
    launch_program()
