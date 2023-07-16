"""

miles to km
"""

from tkinter import *

window = Tk()
window.title("Miles to killometers")
window.minsize(width=225, height=100)
Km_Label = Label(text="Km")
Miles_Label = Label(text="Miles")
is_equal_to = Label(text="is equal to")
is_equal_to.grid(row=1, column=0)
Km_Label.grid(row=1, column=2, pady=2)
Miles_Label.grid(row=0, column=2, pady = 2)
entry = Entry(width=8)
entry.grid(row=0, column=1)
text = Text(height=1, width=6)
text.grid(row=1, column=1)



def action():
    text.delete("1.0", "end")
    text.insert(END, (int(entry.get())* 1.60934))


button = Button(text="Calculate", command=action)
button.grid(row=3, column=1)

window.mainloop()
