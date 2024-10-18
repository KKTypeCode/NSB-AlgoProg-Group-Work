import tkinter as tk
from tkinter import *
from tkinter import ttk

root = tk.Tk()
root.geometry('300x300')
title = Label(root, text="Expense Tracker Page")
title.pack()

def add_expense():
    expense_frame = tk.Frame(root)
    expense_frame.pack(pady=10)

    name_label = tk.Label(expense_frame, text="Expense Name: ")
    name_label.grid(row=0, column=0, padx=5, pady=2)

    name_entry = tk.Entry(expense_frame)
    name_entry.grid(row=0, column=1, padx=5, pady=2)

    amount_label = tk.Label(expense_frame, text="Amount: ")
    amount_label.grid(row=1, column=0, padx=5, pady=2)

    amount_entry = tk.Entry(expense_frame)
    amount_entry.grid(row=1, column=1, padx=5, pady=2)

    type_label = tk.Label(expense_frame, text="Type: ")
    type_label.grid(row=2, column=0, padx=5, pady=2)

    type_entry = tk.Entry(expense_frame)
    type_entry.grid(row=2, column=1, padx=5, pady=2)
add_expense()

# Table

treeview = ttk.Treeview(columns=("amount", "type"))
treeview.heading("#0", text="Name")
treeview.heading("amount", text="Amount")
treeview.heading("type", text="Type")

# Example Table View

treeview.insert(
    "",
    tk.END,
    text="Matcha",
    values=("$3.49", "F&B")
)

treeview.pack()
root.mainloop()
