import random
from tkinter import *
import pandas
BACKGROUND_COLOR = "#B1DDC6"
current_card={}
to_learn={}
from random import choice
try:
 data=pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data=pandas.read_csv("data/french_words.csv")
    to_learn=original_data.to_dict(orient="records")
else:
    to_learn=data.to_dict(orient="records")

# print(to_learn)
def next_card():
    global current_card,filp_timer
    window.after_cancel(filp_timer)
    current_card=random.choice(to_learn)
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    canvas.itemconfig(card_background,image=front_image)
    flip_timer=window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=current_card["English"],fill="white")
    canvas.itemconfig(card_background,image=back_image)
def is_known():
    to_learn.remove(current_card)
    data=pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()
    # print(len(to_learn))
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
filp_timer=window.after(3000,func=flip_card)
canvas = Canvas(width=800, height=526)

front_image = PhotoImage(file="images/card_front.png")
back_image=PhotoImage(file="images/card_back.png")
card_background=canvas.create_image(400, 263, image=front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title=canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word=canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image,command=next_card)
unknown_button.grid(row=1, column=0)
unknown_button.config(highlightthickness=0)
check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image,command=is_known)
known_button.grid(row=1, column=1)
known_button.config(highlightthickness=0)


next_card()


window.mainloop()
