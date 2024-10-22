import tkinter as tk
import subprocess as sp
import pull_transaction as pt
from openpyxl import load_workbook

wb = load_workbook('NSB-AlgoProg-Group-Work/Database.xlsx')
db = wb.active

class FinanceDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Finance Dashboard")
        self.root.geometry("500x400")
        self.root.config(bg="white")
        self.income = db['L3'].value
        self.expenses = db['L4'].value
        self.remain_budget = db['L5'].value - db['L6'].value
        self.header_label = tk.Label(root, text="Finance Dashboard", font=("Arial", 24, "bold"), bg="white")
        self.header_label.pack(pady=10)
        self.create_dashboard()
        self.create_buttons()


    def create_dashboard(self):
        self.income_label = tk.Label(self.root, text="Total Income:", font=("Arial", 16), bg="white")
        self.income_label.place(x=50, y=80)
        self.income_value_label = tk.Label(self.root, text=f"${self.income}", font=("Arial", 16, "bold"), bg="white", fg="green")
        self.income_value_label.place(x=182, y=80)
        self.expense_label = tk.Label(self.root, text="Total Expenses:", font=("Arial", 16), bg="white")
        self.expense_label.place(x=50, y=120)
        self.expense_value_label = tk.Label(self.root, text=f"${self.expenses}", font=("Arial", 16, "bold"), bg="white", fg="red")
        self.expense_value_label.place(x=205, y=120)
        self.remain_budget_label = tk.Label(self.root, text="Remaining Budget:", font=("Arial", 16), bg="white")
        self.remain_budget_label.place(x=50, y=160)
        self.remain_budget_value_label = tk.Label(self.root, text=f"${self.remain_budget}", font=("Arial", 16, "bold"), bg="white", fg="blue")
        self.remain_budget_value_label.place(x=230, y=160)
        self.net_balance = self.income - self.expenses
        self.net_balance_label = tk.Label(self.root, text="Net Balance:", font=("Arial", 16), bg="white")
        self.net_balance_label.place(x=50, y=200)
        net_balance_color = "green" if self.net_balance >= 1000 else "red"
        self.net_balance_value_label = tk.Label(self.root, text=f"${self.net_balance}", font=("Arial", 16, "bold"), bg="white", fg=net_balance_color)
        self.net_balance_value_label.place(x=175, y=200)

    def create_buttons(self):
        self.view_income_button = tk.Button(self.root, text="Budget", font=("Arial", 12), command=lambda:sp.run(["python", "NSB-AlgoProg-Group-Work/budget_page.py"]))
        self.view_income_button.place(x=50, y=260)
        self.view_expenses_button = tk.Button(self.root, text="Entry Input", font=("Arial", 12), command=lambda:'ewduwhdewoide')
        self.view_expenses_button.place(x=160, y=260)
        self.add_transaction_button = tk.Button(self.root, text="Entry Book", font=("Arial", 12), command=lambda:sp.run(["python", "NSB-AlgoProg-Group-Work/transaction_history.py"]))
        self.add_transaction_button.place(x=300, y=260)
        self.add_recurring_button = tk.Button(self.root, text="Add Monthly Expenses", font=("Arial", 12), command=lambda:sp.run(["python", "NSB-AlgoProg-Group-Work/Recurring.py"]))
        self.add_recurring_button.place(x=50, y=300)

    def reset_values(self):
        self.income = 0
        self.expenses = 0
        self.remain_budget = 0
        self.update_dashboard()

    def update_dashboard(self):
        self.income_value_label.config(text=f"${self.income}")
        self.expense_value_label.config(text=f"${self.expenses}")
        self.remain_budget_value_label.config(text=f"${self.remain_budget}")
        self.net_balance = self.income - self.expenses
        net_balance_color = "green" if self.net_balance >= 1000 else "red"
        self.net_balance_value_label.config(text=f"${self.net_balance}", fg=net_balance_color)

if __name__ == "__main__":
    root = tk.Tk()
    app = FinanceDashboard(root)
    root.mainloop()