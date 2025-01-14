from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
data = pandas.read_csv("data/first_500_german_english_words_from_excel.csv")
to_learn = data.to_dict(orient="records")

current_card = {}

# Next card function
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text= "German", fill="black")
    canvas.itemconfig(card_word, text=current_card["German"], fill="black")
    canvas.itemconfig(card_bg, image=card_front_img)
    flip_timer = window.after(5000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_bg, image=card_back_img)
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")

def is_known():
    to_learn.remove(current_card)
    next_card()

# UI setup

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=100, bg = BACKGROUND_COLOR)

flip_timer = window.after(5000, func=flip_card)

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400, 263, image= card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

cross_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
unknown_button.grid(row=1, column=0)

check_img = PhotoImage(file="images/right.png")
known_button = Button(image=check_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_card)
known_button.grid(row=1, column=1)

next_card()
window.mainloop()