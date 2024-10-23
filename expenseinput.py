import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import MainIO as io

class Expense:
    def __init__(self, master, root):
        self.root = root
        self.master = master
        self.master.title("Expense Entry Page")
        self.master.geometry("500x400")
        self.master.config(bg="white")
       
        self.spacing_label = tk.Label(master, text="                      ", bg="white")
        self.spacing_label.pack(pady=35)
        
        self.name_label = tk.Label(master, text="Entry Name:", bg="white")
        self.name_label.pack(pady=5)
        
        self.name_entry = tk.Entry(master)
        self.name_entry.pack(pady=5)

        self.date_label = tk.Label(master, text="Date Period:", bg="white")
        self.date_label.pack(pady=5)
        
        self.date_entry = tk.Entry(master)
        self.date_entry.pack(pady=5)
        
        self.value_label = tk.Label(master, text="Value:", bg="white")
        self.value_label.pack(pady=5)
        
        self.value_entry = tk.Entry(master)
        self.value_entry.pack(pady=5)
        
        self.category_label = tk.Label(master, text="Category:", bg="white")
        self.category_label.pack(pady=5)

        self.category_entry = ttk.Entry(master)
        self.category_entry.pack(pady=5)
        
        self.delivered_label = tk.Label(master, text="Completion of Transaction:", bg="white")
        self.delivered_label.pack(pady=5)
        
        self.delivered_entry = ttk.Entry(master)
        self.delivered_entry.pack(pady=5)
        
        self.calculate_button = tk.Button(master, text="Add your expense", command=self.store_expense)
        self.calculate_button.pack(pady=20)

        self.result_label = tk.Label(master, text="", bg="white")
        self.result_label.pack(pady=5)
        
    def store_expense(self):
        try:
            io.expense(self.name_entry.get(), self.date_entry.get(), self.value_entry.get(), self.category_entry.get(), self.delivered_entry.get())
            self.result_label.config(text=f"Your recurring transaction has been added!")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid inputs for all fields!")

if __name__ == "__main__":
    root = tk.Tk()
    app = Expense(root, root)
    root.mainloop()