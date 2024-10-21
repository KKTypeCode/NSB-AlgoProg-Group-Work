import tkinter as tk
import subprocess as sp

class FinanceDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Finance Dashboard")
        self.root.geometry("500x400")
        self.root.config(bg="white")
        self.income = 5000
        self.expenses = 2000
        self.savings = 3000
        self.header_label = tk.Label(root, text="Finance Dashboard", font=("Arial", 24, "bold"), bg="white")
        self.header_label.pack(pady=10)
        self.create_dashboard()
        self.create_buttons()


    def create_dashboard(self):
        self.income_label = tk.Label(self.root, text="Income:", font=("Arial", 16), bg="white")
        self.income_label.place(x=50, y=80)
        self.income_value_label = tk.Label(self.root, text=f"${self.income}", font=("Arial", 16, "bold"), bg="white", fg="green")
        self.income_value_label.place(x=150, y=80)
        self.expense_label = tk.Label(self.root, text="Expenses:", font=("Arial", 16), bg="white")
        self.expense_label.place(x=50, y=120)
        self.expense_value_label = tk.Label(self.root, text=f"${self.expenses}", font=("Arial", 16, "bold"), bg="white", fg="red")
        self.expense_value_label.place(x=150, y=120)
        self.savings_label = tk.Label(self.root, text="Savings:", font=("Arial", 16), bg="white")
        self.savings_label.place(x=50, y=160)
        self.savings_value_label = tk.Label(self.root, text=f"${self.savings}", font=("Arial", 16, "bold"), bg="white", fg="blue")
        self.savings_value_label.place(x=150, y=160)
        self.net_balance = self.income - self.expenses
        self.net_balance_label = tk.Label(self.root, text="Net Balance:", font=("Arial", 16), bg="white")
        self.net_balance_label.place(x=50, y=200)
        net_balance_color = "green" if self.net_balance >= 0 else "red"
        self.net_balance_value_label = tk.Label(self.root, text=f"${self.net_balance}", font=("Arial", 16, "bold"), bg="white", fg=net_balance_color)
        self.net_balance_value_label.place(x=180, y=200)

    def create_buttons(self):
        self.view_income_button = tk.Button(self.root, text="Budget", font=("Arial", 12), command=lambda:sp.run(["python", "budget_page.py"]))
        self.view_income_button.place(x=50, y=260)
        self.view_expenses_button = tk.Button(self.root, text="I&E", font=("Arial", 12), command=lambda:)
        self.view_expenses_button.place(x=150, y=260)
        self.add_transaction_button = tk.Button(self.root, text="Entry Book", font=("Arial", 12), command=lambda:sp.run(["python", "transaction_history.py"]))
        self.add_transaction_button.place(x=280, y=260)
        self.reset_values_button = tk.Button(self.root, text="Reset Data", font=("Arial", 12), command=self.reset_values)
        self.reset_values_button.place(x=380, y=260)

    def reset_values(self):
        self.income = 0
        self.expenses = 0
        self.savings = 0
        self.update_dashboard()

    def update_dashboard(self):
        self.income_value_label.config(text=f"${self.income}")
        self.expense_value_label.config(text=f"${self.expenses}")
        self.savings_value_label.config(text=f"${self.savings}")
        self.net_balance = self.income - self.expenses
        net_balance_color = "green" if self.net_balance >= 0 else "red"
        self.net_balance_value_label.config(text=f"${self.net_balance}", fg=net_balance_color)

if __name__ == "__main__":
    root = tk.Tk()
    app = FinanceDashboard(root)
    root.mainloop()