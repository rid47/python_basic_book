'''

Write a program that simulates rolling a six-sided die. There
should be one button with the text "Roll". When the user clicks
the button, a random integer from 1 to 6 should be displayed.

'''

import tkinter as tk
import random


def roll():
    # print('change label text')
    
    label['text']=str(random.randint(1,6))
    
window = tk.Tk()


window.columnconfigure(0, minsize=150)
window.rowconfigure([0,1], minsize=50)

btn_roll = tk.Button(text='Roll', command=roll)

label = tk.Label()


btn_roll.grid(row=0, column=0, sticky='nsew')
label.grid(row=1, column=0)

window.mainloop()