from tkinter import *
import json
import random
import pandas as pd


BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courier"
dict_data = {}
known_f_word = ""
known_e_word = ""
known_words = []
current_card = {}
to_learn = {}

# #----------------------------------- create json data ------------------------------------------------#
try:
    data = pd.read_csv("./data/unknown_words.csv")
except FileNotFoundError:
    original_data = pd.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')

#---------------------------- cards management ----------------------------------------------------------#
def next_card():
    global current_card, flip_timer
    window_main.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas_scr.itemconfig(canvas_background, image=card_front_image)
    canvas_scr.itemconfig(lang_text, text="French", fill="black")
    canvas_scr.itemconfig(word_text, text=current_card["French"],fill="black")
    window_main.after(3000, flip_the_card)

def flip_the_card():
    canvas_scr.itemconfig(canvas_background, image=card_back_image)
    canvas_scr.itemconfig(lang_text, text="English", fill="white")
    canvas_scr.itemconfig(word_text, text=current_card["English"], fill="white")

def is_known():
    print(len(to_learn))
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("./data/unknown_words.csv")
    next_card()

#------------------------------- UI SET UP ---------------------------------------------------------#
window_main = Tk()
window_main.title("Flashy")
window_main.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window_main.after(3000, flip_the_card)

canvas_scr = Canvas(width=800, height=526, highlightthickness=0)
canvas_right = Canvas(width=10, height=10, highlightthickness=0)
canvas_wrong = Canvas(width=10, height=10, highlightthickness=0)
card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")
canvas_background = canvas_scr.create_image(400, 263, image=card_front_image)
canvas_scr.config(bg=BACKGROUND_COLOR)
canvas_scr.grid(row=0, column=0, columnspan=2)

lang_text = canvas_scr.create_text(400, 158, text="Title", font=("Arial", 48, "italic"))
word_text = canvas_scr.create_text(400, 263, text="word", font=("Arial", 48, "bold"))

#cross image
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, command=next_card, highlightthickness=0)
wrong_button.grid(row=1, column=0)

#check image
right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, command=is_known, highlightthickness=0)
right_button.grid(row=1, column=1)

next_card()
window_main.mainloop()
