from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"

df = pd.read_csv('data/french_words.csv')
words = df.to_dict()

def next_card():
    int = random.randint(0,100)
    french_word = words['French'][int]
    canvas.itemconfig(card_title,text = "French")
    canvas.itemconfig(card_word, text=french_word)
#
window = Tk()
window.title("Flashy")
window.configure(padx=50,pady=50,background=BACKGROUND_COLOR)

canvas = Canvas(width=800,height=526)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400,263,image=card_front_img)
card_title = canvas.create_text(400,150,text='',font=("Arial",40,"italic"),fill="black")
card_word = canvas.create_text(400,263,text='',font=("Arial",60,"bold"),fill='black')
canvas.configure(background=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row =0,column=0,columnspan=2)

right = PhotoImage(file="images/right.png")
button = Button(image=right,highlightthickness=0,command=next_card)
button.grid(row=1,column=1)

wrong = PhotoImage(file="images/wrong.png")
button = Button(image=wrong,highlightthickness=0,command=next_card)
button.grid(row=1,column=0)

next_card()

window.mainloop()