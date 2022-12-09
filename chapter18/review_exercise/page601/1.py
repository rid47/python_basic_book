'''
Write a program that displays a single button with the default
background color and black text that reads "Click me".
When the user clicks the button, the button background should
change to a color randomly selected from the following list:

["red", "orange", "yellow", "blue", "green", "indigo", "violet"]

'''

import tkinter as tk
import random

def change_bg():
    # print('button clicked')
    color_list = ["red", "orange", "yellow", "blue", "green", "indigo", "violet"]
    color = random.choice(color_list)
    button.configure(bg=color)

window = tk.Tk()


button = tk.Button(master=window, text='click me',fg='black', command=change_bg)
button.pack()


window.mainloop()