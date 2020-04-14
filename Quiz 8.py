from tkinter import *
from math import *

root = Tk()
root.wm_title("Quiz 8")

class Application(Frame):
    global a, b

    # create the box for user input 
    frame1 = Frame(root)
    frame1.pack()

    #box for number a
    Label(frame1, text="Number A").grid(row=0, column=0, sticky=W)
    a = IntVar()
    a = Entry(frame1, textvariable = a )
    a.grid(row=0, column=1, sticky=W)

    #box for number b
    Label(frame1, text="Number B").grid(row=1, column=0, sticky=W)
    b = IntVar()
    b = Entry(frame1, textvariable = b)
    b.grid(row=1, column=1, sticky=W)
    
    #calculation function
    def multiplication(self):
        output = StringVar()
        output.set(a.get() + " * " + b.get() + " = " \
                   + str(int(a.get()) * int(b.get()))) #set output for label statement below
        label = Label(root, textvariable = output) #textvariable will print variable output
        label.pack()
        
    def division(self):
        output = StringVar()
        output.set(a.get() + " / " + b.get() + " = " \
                   + str(int(a.get()) / int(b.get())))
        label = Label(root, textvariable = output)
        label.pack()
        
    def summation(self):
        output = StringVar()
        output.set(a.get() + " + " + b.get() + " = " \
                   + str(int(a.get()) + int(b.get())))
        label = Label(root, textvariable = output)
        label.pack()
        
    def subtraction(self):
        output = StringVar()
        output.set(a.get() + " - " + b.get() + " = " \
                   + str(int(a.get()) - int(b.get())))
        label = Label(root, textvariable = output)
        label.pack()
        
    def squareroot(self):
        output1 = StringVar()
        output1.set("Square root of " + a.get() + " = "\
                   + str(sqrt(int(a.get()))))
        label1 = Label(root, textvariable = output1)
        label1.pack()
        
        output2 = StringVar()
        output2.set("Square root of " + b.get() + " = "\
                   + str(sqrt(int(b.get()))))
        label2 = Label(root, textvariable = output2)
        label2.pack()

    # create the button option for user
    def createWidgets(self):

        #multiply button
        self.multiply = Button(self)
        self.multiply["text"] = "Multiply"
        self.multiply["fg"] = "blue"
        self.multiply["command"] = self.multiplication

        self.multiply.pack({"side": "left"})

        #divide button
        self.divide = Button(self)
        self.divide["text"] = "Divide"
        self.divide["fg"] = "blue"
        self.divide["command"] = self.division

        self.divide.pack({"side": "left"})

        #addition button
        self.add = Button(self)
        self.add["text"] = "Add"
        self.add["fg"] = "blue"
        self.add["command"] = self.summation

        self.add.pack({"side": "left"})

        #subtract button
        self.subtract = Button(self)
        self.subtract["text"] = "Subtract"
        self.subtract["fg"] = "blue"
        self.subtract["command"] = self.subtraction

        self.subtract.pack({"side": "left"})

        #sqrt button
        self.sqrt = Button(self)
        self.sqrt["text"] = "Sqrt"
        self.sqrt["fg"] = "blue"
        self.sqrt["command"] = self.squareroot

        self.sqrt.pack({"side": "left"})

        #quit button
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

#name and main window
if __name__ == "__main__":
    app = Application(master = root)
    app.mainloop()
    root.destroy()
