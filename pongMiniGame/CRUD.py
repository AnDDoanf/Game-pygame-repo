from tkinter import *

window = Tk()
window.wm_title("Book shop")

l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l1 = Label(window, text="Author")
l1.grid(row=0, column=2)

l1 = Label(window, text="Year")
l1.grid(row=1, column=0)

l1 = Label(window, text="ISBN")
l1.grid(row=1, column=2)

title_text = StringVar()
ent1 = Entry(window, textvariable=title_text)
ent1.grid(row=0, column=1)

window.mainloop()