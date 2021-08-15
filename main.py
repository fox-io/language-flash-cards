"""
language-flash-cards

(c)2021 John Mann <github.fox-io@foxdata.io>
"""
import tkinter
import random
import pandas


class LanguageFlashCards:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Language Flash Cards")
        self.window.config(
            padx=50,
            pady=50,
            bg="#aed9c2"
        )

        self.canvas = tkinter.Canvas(
            width=800,
            height=526,
            highlightthickness=0,
            bg="#aed9c2"
        )
        self.card_front = tkinter.PhotoImage(file="./images/card_front.png")
        self.card_back = tkinter.PhotoImage(file="./images/card_back.png")
        self.card_image = self.canvas.create_image(800/2, 526/2, image=self.card_front)
        self.language_text = self.canvas.create_text(
            400,
            150,
            text="Language",
            fill="black",
            font=("Arial", 40, "italic")
        )
        self.word_text = self.canvas.create_text(
            400,
            263,
            text="Word",
            fill="black",
            font=("Arial", 60, "bold")
        )
        self.canvas.grid(row=0, column=0, columnspan=2)

        self.right_image = tkinter.PhotoImage(file="./images/right.png")
        self.right_button = tkinter.Button(
            image=self.right_image,
            highlightthickness=0,
            command=self.right_button_onclick
        )
        self.right_button.grid(column=1, row=1)

        self.wrong_image = tkinter.PhotoImage(file="./images/wrong.png")
        self.wrong_button = tkinter.Button(
            image=self.wrong_image,
            highlightthickness=0,
            command=self.wrong_button_onclick
        )
        self.wrong_button.grid(column=0, row=1)

        self.language_0 = None
        self.language_1 = None
        self.language_dict = {}
        self.load_language_cards()

        self.timer = None
        self.current_card = None
        self.get_new_card()

        self.FRONT = 0
        self.BACK = 1
        self.set_word_label(self.FRONT)

    def load_language_cards(self):
        try:
            language_data = pandas.read_csv("./data/to_learn.csv")
        except FileNotFoundError:
            language_data = pandas.read_csv("./data/french_words.csv")
        self.language_dict = language_data.to_dict(orient='records')

    def remove_card(self):
        self.language_dict.remove(self.current_card)
        save_data = pandas.DataFrame(self.language_dict)
        save_data.to_csv('./data/to_learn.csv')

    def get_new_card(self):
        self.current_card = random.choice(self.language_dict)
        self.start_timer()

    def set_word_label(self, side):
        if side == self.FRONT:
            self.canvas.itemconfigure(self.language_text, text="French")
            self.canvas.itemconfigure(self.word_text, text=self.current_card["French"])
            self.canvas.itemconfigure(self.card_image, image=self.card_front)
        else:
            self.canvas.itemconfigure(self.language_text, text="English")
            self.canvas.itemconfigure(self.word_text, text=self.current_card["English"])
            self.canvas.itemconfigure(self.card_image, image=self.card_back)

    def right_button_onclick(self):
        self.remove_card()
        self.window.after_cancel(self.timer)
        self.get_new_card()
        self.set_word_label(self.FRONT)

    def wrong_button_onclick(self):
        self.window.after_cancel(self.timer)
        self.get_new_card()
        self.set_word_label(self.FRONT)

    def start_timer(self):
        self.timer = self.window.after(3000, self.ontimer)

    def ontimer(self):
        self.set_word_label(self.BACK)


if __name__ == "__main__":
    app = LanguageFlashCards()
    app.window.mainloop()
