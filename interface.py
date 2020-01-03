from Tkinter import *

class Interface:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.exit = Button(
            frame, text="Exit", fg="blue", command=frame.quit
            )
        self.button.pack(side=LEFT)

        self.generate = Button(frame, text="Generate", command=randomiser.mixer())
        self.hi_there.pack(side=LEFT)

root = Tk()

app = Interface(root)

root.mainloop()

root.distroy()
