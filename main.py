from tkinter import *


BACKGROUND_COLOR = "#B1DDC6"

# UI setup

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=100, bg = BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image= card_front_img)
canvas.create_text(400, 150, text="Titel", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

cross_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_img, highlightthickness=0, bg=BACKGROUND_COLOR)
unknown_button.grid(row=1, column=0)

check_img = PhotoImage(file="images/right.png")
known_button = Button(image=check_img, highlightthickness=0, bg=BACKGROUND_COLOR)
known_button.grid(row=1, column=1)


window.mainloop()