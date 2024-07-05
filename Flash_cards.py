from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_word = {}
to_learn = []

try:
    data = pd.read_csv("data/french_words.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_word.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_word():
    global current_word, flip_timer
    window.after_cancel(flip_timer)  # Cancel the previous flip timer
    current_word = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_word["French"])
    canvas.itemconfig(card_image, image=card_front)
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=current_word["English"])
    canvas.itemconfig(card_image, image=card_back)

def is_know():
    global to_learn
    if current_word in to_learn:
        to_learn.remove(current_word)
        print(len(to_learn))
        data = pd.DataFrame(to_learn)
        data.to_csv("data/words_to_learn.csv", index=False)
    next_word()

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Create canvas
canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_img = PhotoImage(file="images/wrong.png")
right_img = PhotoImage(file="images/right.png")

unknown_button = Button(image=wrong_img, highlightthickness=0, command=is_know)
unknown_button.grid(row=1, column=0)

known_button = Button(image=right_img, highlightthickness=0, command=next_word)
known_button.grid(row=1, column=1)

flip_timer = window.after(3000, flip_card)  # Initialize the timer

next_word()

window.mainloop()
