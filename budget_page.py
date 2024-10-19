import tkinter as tk
from tkinter import messagebox

class BudgetPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Budget Page")

        self.income_label = tk.Label(master, text="                      ")
        self.income_label.pack(pady=70)
        
        self.income_label = tk.Label(master, text="Monthly Income:")
        self.income_label.pack(pady=5)

        self.expense_label = tk.Label(master, text="Monthly Expenses:")
        self.expense_label.pack(pady=5)

        
        self.income_entry = tk.Entry(master)
        self.income_entry.pack(pady=5)

        self.expense_entry = tk.Entry(master)
        self.expense_entry.pack(pady=5)

        
        self.calculate_button = tk.Button(master, text="Calculate Remaining Budget", command=self.calculate_budget)
        self.calculate_button.pack(pady=20)

        
        self.result_label = tk.Label(master, text="")
        self.result_label.pack(pady=5)

    def calculate_budget(self):
        try:
            income = float(self.income_entry.get())
            expenses = float(self.expense_entry.get())
            remaining_budget = income - expenses

            self.result_label.config(text=f"Remaining Budget: ${remaining_budget:.2f}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for income and expenses")

if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetPage(root)
    root.mainloop()