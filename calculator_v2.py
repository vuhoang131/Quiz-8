from tkinter import *
import math

expression = ""

# input entry box 
def press(num): 
    global expression 
    expression = expression + str(num) 
    equation.set(expression) 


# equal button 
def equalButton():
    global expression
    try:
        total = str(eval(expression))
        expression = equation
    except:
        equation.set(" error ") 
    equation.set(total)  

# clear button
def clearButton(): 
    global expression 
    expression = "" 
    equation.set("") 


# Driver code 
def main_function():
    global equation
    root = Tk() 
    root.configure(background="gray") 
    root.title("Quiz 8 calculator") 
    root.geometry("265x125")  
    equation = StringVar() 
    expression_field = Entry(root, textvariable=equation) 
    expression_field.grid(columnspan=4, ipadx=70)
    equation.set('enter your expression') 

    #create button
    button1 = Button(root, text=' 1 ', fg='black',
                     command=lambda: press(1), height=1, width=7)  
    button2 = Button(root, text=' 2 ', fg='black',
                     command=lambda: press(2), height=1, width=7)
    button3 = Button(root, text=' 3 ', fg='black',
                     command=lambda: press(3), height=1, width=7)
    
    button4 = Button(root, text=' 4 ', fg='black', 
					command=lambda: press(4), height=1, width=7)
    button5 = Button(root, text=' 5 ', fg='black',
                     command=lambda: press(5), height=1, width=7)
    button6 = Button(root, text=' 6 ', fg='black',
                     command=lambda: press(6), height=1, width=7)
    
    button7 = Button(root, text=' 7 ', fg='black',
                     command=lambda: press(7), height=1, width=7)
    button8 = Button(root, text=' 8 ', fg='black',
                     command=lambda: press(8), height=1, width=7)
    button9 = Button(root, text=' 9 ', fg='black',
                     command=lambda: press(9), height=1, width=7)
    
    button0 = Button(root, text=' 0 ', fg='black',
                     command=lambda: press(0), height=1, width=7)

    #operator button
    plus = Button(root, text=' + ', fg='black',
                  command=lambda: press("+"), height=1, width=7)
    minus = Button(root, text=' - ', fg='black',
                   command=lambda: press("-"), height=1, width=7)
    multiply = Button(root, text=' * ', fg='black',
                      command=lambda: press("*"), height=1, width=7)
    divide = Button(root, text=' / ', fg='black',
                    command=lambda: press("/"), height=1, width=7)
    equal = Button(root, text=' = ', fg='black',
                   command = equalButton, height=1, width=7)
    clear = Button(root, text = 'Clear', fg='black',
                   command = clearButton, height=1, width=7)
    

    #put button in order
    button1.grid(row=2, column=0)
    button2.grid(row=2, column=1)
    button3.grid(row=2, column=2)

    button4.grid(row=3, column=0)
    button5.grid(row=3, column=1)
    button6.grid(row=3, column=2)

    button7.grid(row=4, column=0)
    button8.grid(row=4, column=1)
    button9.grid(row=4, column=2)

    button0.grid(row=5, column=0)
    plus.grid(row=2, column=3)
    minus.grid(row=3, column=3)
    multiply.grid(row=4, column=3)
    divide.grid(row=5, column=3)
    equal.grid(row=5, column=2)
    clear.grid(row=5, column= 1)

    root.mainloop()
    
if __name__ == "__main__":
    main_function()
