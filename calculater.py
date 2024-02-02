import tkinter as tk

def add():
    result = int(number_1.get()) + int(number_2.get())
    result_text.set(result)

def subtract():
    result = int(number_1.get()) - int(number_2.get())
    result_text.set(result)

def multiply():
    result = int(number_1.get()) * int(number_2.get())
    result_text.set(result)

def divide():
    if number_2.get() != 0:
        result = int(number_1.get()) / int(number_2.get())
        result_text.set(result)
    else:
        result_text.set("Error: Division by zero is not allowed.")

root = tk.Tk()
root.title("Simple Calculator")

number_1 = tk.StringVar()
number_2 = tk.StringVar()
result_text = tk.StringVar()

entry_1 = tk.Entry(root, textvariable=number_1)
entry_1.grid(row=0, column=0)

entry_2 = tk.Entry(root, textvariable=number_2)
entry_2.grid(row=0, column=1)

add_button = tk.Button(root, text="+", command=add)
add_button.grid(row=1, column=0)

subtract_button = tk.Button(root, text="-", command=subtract)
subtract_button.grid(row=1, column=1)

multiply_button = tk.Button(root, text="*", command=multiply)
multiply_button.grid(row=2, column=0)

divide_button = tk.Button(root, text="/", command=divide)
divide_button.grid(row=2, column=1)

result_label = tk.Label(root, textvariable=result_text)
result_label.grid(row=3, column=0, columnspan=2)

root.mainloop()