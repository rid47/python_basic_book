import tkinter as tk

window = tk.Tk()

frame_a = tk.Frame()

label1 = tk.Label(master=frame_a, text="I am in frame_a")

label1.pack()
frame_a.pack()




window.mainloop()