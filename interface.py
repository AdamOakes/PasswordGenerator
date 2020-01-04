from Tkinter import *

class Interface:
    
    passLen = entry.get()
    upperVal = upperCase()
    lowerVal = lowerCase()
    symVal = symbol()
    numVal = number()

    window = Tk()
    window.title('Password Generator')
    #this is a some test text for git
    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        # Check boxes:
        book_1 = CheckButton(frame, text = 'Uppercase', \
                                variable = upperVal, onvalue = 1, offvalue = 0)
        book_2 = CheckButton(frame, text = 'Lowercase', \
                                variable = lowerVal, onvalue = 1, offvalue = 0)
        book_3 = CheckButton(frame, text = 'Symbols', \
                                variable = symVal, onvalue = 1, offvalue = 0)
        book_4 = CheckButton(frame, text = 'Numbers', \
                                variable = numVal, onvalue = 1, offvalue = 0)
        book_1.pack(side = LEFT)
        book_2.pack(side = LEFT)
        book_3.pack(side = LEFT)
        book_4.pack(side = LEFT)
        
        # Input field:
        self.length = field()
        
        entry = Entry(frame)

        self.exit = Button(
            frame, text="Exit", fg="blue", command=frame.quit
            )
        self.button.pack(side=LEFT)

        self.generate = Button(frame, text="Generate", command=Randomiser.mixer(passLen))
        self.hi_there.pack(side=LEFT)

root = Tk()

app = Interface(root)

root.mainloop()

root.distroy()
