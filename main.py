"""
language-flash-cards

(c)2021 John Mann <github.fox-io@foxdata.io>
"""
import tkinter
import csv
import random


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
        self.canvas.create_image(800/2, 526/2, image=self.card_front)
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
        self.right_button = tkinter.Button(image=self.right_image, highlightthickness=0)
        self.right_button.grid(column=1, row=1)

        self.wrong_image = tkinter.PhotoImage(file="./images/wrong.png")
        self.wrong_button = tkinter.Button(image=self.wrong_image, highlightthickness=0)
        self.wrong_button.grid(column=0, row=1)

        self.language = {}
        self.load_language_cards()

        self.get_random_card()

    def load_language_cards(self):
        with open("./languages/french_words.csv") as language_file:
            language_data = csv.reader(language_file)
            for row in language_data:
                # Crude method of skipping the first header row in the csv file.
                if row[0] != "French":
                    self.language[row[0]] = row[1]

    def get_random_card(self):
        pass


if __name__ == "__main__":
    app = LanguageFlashCards()
    app.window.mainloop()
