import algorithm 
import tkinter as tk
from tkinter import messagebox #madtrsh eny aktb tk.messagebox kol mara

# Linear search algorithm click event
def linear_search_click():
    data_str = data_entry.get() #textbox el baktb fee
    target_str = target_entry.get() 

    try:
        data = [int(x) for x in data_str.split(',')]  #b7wlhom mn strn to intgar
        target = int(target_str)
        result = algorithm.linear_search(data, target)

        if result != -1:
            messagebox.showinfo("Linear Search Result", result)
        else:
            result_label.config(text="Target not found.")
    except ValueError:
        result_label.config(text="Invalid input. Please enter comma-separated numbers.")

# Selection sort algorithm click event
def selection_sort_click():
    data_str = data_entry.get()

    try:
        data = [int(x) for x in data_str.split(',')]
        result = algorithm.selection_sort(data)
        messagebox.showinfo("Selection Sort Result", result)
    except ValueError:
        result_label.config(text="Invalid input. Please enter comma-separated numbers.")

# Binary search algorithm click event
def binary_search_click():
    data_str = data_entry.get()
    target_str = target_entry.get()

    try:
        data = [int(x) for x in data_str.split(',')]
        target = int(target_str)
        result = algorithm.binary_search(data, target)

        if result != -1:
            messagebox.showinfo("Binary Search Result", result)
        else:
            result_label.config(text="Target not found")
    except ValueError:
        result_label.config(text="Invalid input. Please enter comma-separated numbers.")

# Bubble sort algorithm click event
def bubble_sort_click():
    data_str = data_entry.get()

    try:
        data = [int(x) for x in data_str.split(',')]
        result = algorithm.bubble_sort(data)
        messagebox.showinfo("Bubble Sort Result", result)
    except ValueError:
        result_label.config(text="Invalid input. Please enter comma-separated numbers.")

# GUI setup
window = tk.Tk() #create window
window.title("Search and Sort App")
window.geometry("600x600")
window.configure(bg="#2c3e50") 

# Gradient background
canvas = tk.Canvas(window, width=400, height=300) #blue el f nos hwa canvas
canvas.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
canvas.create_rectangle(0, 0, 400, 300, fill="#3498db")

data_label = tk.Label(window, text="Enter data (comma-separated):", bg="#3498db", fg="white")
data_label.place(relx=0.5, rely=0.35, anchor=tk.CENTER)
data_entry = tk.Entry(window, bg="#2c3e50",fg="white", width=30)
data_entry.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

target_label = tk.Label(window, text="Enter target to search:", bg="#3498db", fg="white")
target_label.place(relx=0.5, rely=0.45, anchor=tk.CENTER)
target_entry = tk.Entry(window, bg="#2c3e50", fg="white", width=30)
target_entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  

# Buttons
buttons_frame = tk.Frame(window, bg="#3498db")
buttons_frame.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

linear_button = tk.Button(buttons_frame, text="Linear Search", command=linear_search_click, bg="#2c3e50", fg="white", width=12)
linear_button.grid(row=0, column=0, padx=10, pady=5)

selection_button = tk.Button(buttons_frame, text="Selection Sort", command=selection_sort_click, bg="#2c3e50", fg="white", width=12)
selection_button.grid(row=0, column=1, padx=10, pady=5)

binary_button = tk.Button(buttons_frame, text="Binary Search", command=binary_search_click, bg="#2c3e50", fg="white", width=12)
binary_button.grid(row=1, column=0, padx=10, pady=5)

bubble_button = tk.Button(buttons_frame, text="Bubble Sort", command=bubble_sort_click, bg="#2c3e50", fg="white", width=12)
bubble_button.grid(row=1, column=1, padx=10, pady=5)

# Result Label
result_label = tk.Label(window, text="", width=50, bg="#2c3e50", fg="white")
result_label.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

window.mainloop()