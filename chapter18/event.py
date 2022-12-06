from tkinter import Tk, Button


window = Tk()




def handle_keypress(event):
    print(event.char)
    


def handle_click(event):
    print("Button clicked")

window.bind("<Key>", handle_keypress)


button = Button(master=window,text="submit")
button.pack()
button.bind("<Button-3>", handle_click)


window.mainloop()

