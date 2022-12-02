import tkinter as tk


window = tk.Tk()

text_box = tk.Text()

content = text_box.get("1.0")

text_box.pack()

window.mainloop()

print(content)