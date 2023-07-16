"""

playground
"""

from tkinter import *

window = Tk()
window.title("Gui")
window.minsize(500, 300)


my_label = Label(text="I am a label", font=("Arial,", 24, "bold"))
my_label.pack()

my_label["text"] = "new text"
my_label.config(text="new text")


def button_clicked():
    my_label["text"] = input.get()


input = Entry(width=10)
input.pack()
button = Button(text="click me", command=button_clicked)
button.pack()
input.get()


#entry












window.mainloop()
