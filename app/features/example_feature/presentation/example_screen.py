from tkinter import *

class Example:
    def __init__(self, master=None):
        self.linha1 = Frame(master)
        self.linha1["pady"] = 20
        self.linha1.pack()

        self.linha2 = Frame(master)
        self.linha2.pack()

        self.label1 = Label(self.linha1, text="Label Widget")
        self.label1.pack(side=LEFT)
        self.entry1 = Entry(self.linha1)
        self.entry1.pack(side=LEFT)

        self.button1 = Button(self.linha2, text="Button Text", command=self.buttonFunction)
        self.button1.pack()

    def buttonFunction(self):
        print(self.entry1.get())

root = Tk()
Example(root)
print(root.mainloop())
