from tkinter import *

def Calculation ():
    try:
        num1 = float(number1.get())
        num2 = float(number2.get())
    except ValueError :
        result_label.config(text="Invalid Input")
        
    operation = operation_button.get()
    
    if operation == "+":
        result = num1 + num2
        result_label.config(text="Result of Addition : " + str(result))

    elif operation == "-":
        result = num1 - num2
        result_label.config(text="Result of Subtraction : " + str(result))

    elif operation == "*":
        result = num1 * num2
        result_label.config(text="Result of Multiplication : " + str(result))

    elif operation == "/":
        if num2 != 0.0:
            result = num1 / num2
            result_label.config(text="Result of Division: " + str(result))

        else:
            result_label.config(text="Cannot divide by zero")



root = Tk()
root.title("Calculator")

label = Label(root, text="Simple Calculator",background="Blue",font=("Times New Roman",60))
label.pack(fill= BOTH)

label = Label(root, text="Enter the Numbers",background="white",font=("Times New Roman",30))
label.pack()

label = Label(root, text="Enter a First Number:",font=("Times New Roman",20))
label.place(x=550,y=160)

number1 = Entry(root, width=30,font=(7))
number1.place(x=850,y=170)

label = Label(root, text="Enter a Second Number:",font=("Times New Roman",20))
label.place(x=550,y=200)

number2 = Entry(root, width=30,font=(7))
number2.place(x=850,y=210)

operation_button = StringVar()
#Add
add_button = Radiobutton(root, text="Addition", variable=operation_button, value="+")
add_button.place(x=750,y=250)
#Subtract
subtract_button = Radiobutton(root, text="Subtraction", variable=operation_button, value="-")
subtract_button.place(x=750,y=270)
#multipy
multiply_button = Radiobutton(root, text="Multiplication", variable=operation_button, value="*")
multiply_button.place(x=750,y=290)
#division
divide_button = Radiobutton(root, text="Division", variable=operation_button, value="/")
divide_button.place(x=750,y=310)

# Calculate button
calculate_button = Button(root, text="Calculate", command=Calculation,height=2,width=10)
calculate_button.place(x=750,y=340)

result_label = Label(root, text="Result: ",font=("Times New Roman",17))
result_label.place(x=750,y=400)

root.mainloop()