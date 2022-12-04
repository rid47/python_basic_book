'''

Write a program that displays an Entry widget that is forty text
units wide and has a white background and black text. Use
.insert() to display text in the Entry widget that reads "What is
your name?"

'''

import tkinter as tk


window = tk.Tk()

ent = tk.Entry(width=40, bg='white',fg='black')
ent.pack()
ent.insert(0,'What is your name?')
window.mainloop()