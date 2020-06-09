from tkinter import *
name = "User"


def ActionClick():
	label = ""
	label = Label(text=entry.get()).grid(row=2,column=1)
	entry.delete(0, END)


root = Tk()
greeting = Label(text=f"Hello, {name}", font="1")
close = Button(root,text="Close", command=root.destroy, fg="red")
action = Button(root,text="Action", command=ActionClick)
entry = Entry(width=10)


greeting.grid(row=0,column=0, columnspan=2)
close.grid(row=1,column=0)
action.grid(row=1,column=1)
entry.grid(row=3,columnspan=2)

root.mainloop()

