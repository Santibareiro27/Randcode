import tkinter

window = tkinter.Tk()
window.title("Calculator")
window.resizable(False,False)

i = 0

#Entry
text_entry = tkinter.Entry(window, font = ('Calibri 14'), justify = 'right')
text_entry.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 5)

#Functions
def button_pressed(value):
    global i
    text_entry.insert(i, value)
    i += 1

def delete():
    text_entry.delete(0, tkinter.END)
    i = 0

def operate():
    ecuation = text_entry.get()
    result = eval(ecuation)
    text_entry.delete(0, tkinter.END)
    if result == int(result):
        result = int(result)
    text_entry.insert(0, result)
    i = 0

#Buttons
button1 = tkinter.Button(window, text = '1', width = 5, height = 2, command = lambda: button_pressed(1))
button2 = tkinter.Button(window, text = '2', width = 5, height = 2, command = lambda: button_pressed(2))
button3 = tkinter.Button(window, text = '3', width = 5, height = 2, command = lambda: button_pressed(3))
button4 = tkinter.Button(window, text = '4', width = 5, height = 2, command = lambda: button_pressed(4))
button5 = tkinter.Button(window, text = '5', width = 5, height = 2, command = lambda: button_pressed(5))
button6 = tkinter.Button(window, text = '6', width = 5, height = 2, command = lambda: button_pressed(6))
button7 = tkinter.Button(window, text = '7', width = 5, height = 2, command = lambda: button_pressed(7))
button8 = tkinter.Button(window, text = '8', width = 5, height = 2, command = lambda: button_pressed(8))
button9 = tkinter.Button(window, text = '9', width = 5, height = 2, command = lambda: button_pressed(9))
button0 = tkinter.Button(window, text = '0', width = 13, height = 2, command = lambda: button_pressed(0))

button_left_bracket = tkinter.Button(window, text = '(', width = 5, height = 2, command = lambda: button_pressed('('))
button_right_bracket = tkinter.Button(window, text = ')', width = 5, height = 2, command = lambda: button_pressed(')'))
button_delete = tkinter.Button(window, text = 'AC', width = 5, height = 2, command = lambda: delete())
button_dott = tkinter.Button(window, text = '.', width = 5, height = 2, command = lambda: button_pressed('.'))

button_div = tkinter.Button(window, text = chr(247), width = 5, height = 2, command = lambda: button_pressed('/'))
button_mul = tkinter.Button(window, text = 'x', width = 5, height = 2, command = lambda: button_pressed('*'))
button_add = tkinter.Button(window, text = '+', width = 5, height = 2, command = lambda: button_pressed('+'))
button_sub = tkinter.Button(window, text = '-', width = 5, height = 2, command = lambda: button_pressed('-'))
button_equ = tkinter.Button(window, text = '=', width = 5, height = 2, command = lambda: operate())

#Add buttons on screen
#button.grid(row = 0, column = 0, padx = 5, pady = 5)
button_left_bracket.grid(row = 1, column = 0, padx = 5, pady = 5)
button_right_bracket.grid(row = 1, column = 1, padx = 5, pady = 5)
button_delete.grid(row = 1, column = 2, padx = 5, pady = 5)
button_div.grid(row = 1, column = 3, padx = 5, pady = 5)

button7.grid(row = 2, column = 0, padx = 5, pady = 5)
button8.grid(row = 2, column = 1, padx = 5, pady = 5)
button9.grid(row = 2, column = 2, padx = 5, pady = 5)
button_mul.grid(row = 2, column = 3, padx = 5, pady = 5)

button4.grid(row = 3, column = 0, padx = 5, pady = 5)
button5.grid(row = 3, column = 1, padx = 5, pady = 5)
button6.grid(row = 3, column = 2, padx = 5, pady = 5)
button_add.grid(row = 3, column = 3, padx = 5, pady = 5)

button1.grid(row = 4, column = 0, padx = 5, pady = 5)
button2.grid(row = 4, column = 1, padx = 5, pady = 5)
button3.grid(row = 4, column = 2, padx = 5, pady = 5)
button_sub.grid(row = 4, column = 3, padx = 5, pady = 5)

button0.grid(row = 5, column = 0, columnspan = 2, padx = 5, pady = 5)
button_dott.grid(row = 5, column = 2, padx = 5, pady = 5)
button_equ.grid(row = 5, column = 3, padx = 5, pady = 5)

window.mainloop()