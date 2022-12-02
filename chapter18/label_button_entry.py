import tkinter as tk

window = tk.Tk()

display_text = tk.Label(text="hello, tkinter label", fg='black',bg='white',height=5, width=20)

display_button = tk.Button(text="click me!", fg='yellow',bg='red', height=4,width=10)

entry_box = tk.Entry(fg='yellow', bg='blue', width=50)

entry_box.insert(0,"Your name here")
entered_text= entry_box.get()

display_text.pack()
display_button.pack()
entry_box.pack()

# print(f"{entry_box.get()}")

window.mainloop()

print(entered_text)