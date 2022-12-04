'''
Write a program that displays a Button widget that is fifty text units
wide and twenty-five text units tall. 
It should have a white background with blue text that reads "Click here".

'''

import tkinter as tk


window = tk.Tk()
btn = tk.Button(width=50,height=25, bg='white',fg='blue', text='Click here')
btn.pack()

window.mainloop()
