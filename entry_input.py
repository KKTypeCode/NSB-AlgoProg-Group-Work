import tkinter as tk
import subprocess as sp

class EntryInput:
    def __init__(self, master):
        self.master = master
        self.master.title("Entry Input")
        self.master.geometry("500x400")
        self.master.config(bg="white")
        self.spacing = '                     '
        self.spacing_label = tk.Label(self.master, text=self.spacing, bg="white")
        self.spacing_label.pack(pady=50)
        self.income_button = tk.Button(self.master, text="Income", font=("Arial", 20, "bold"), command=lambda:sp.run(['python', 'NSB-AlgoProg-Group-Work/incomeinput.py']))
        self.income_button.pack(pady=10)
        self.spacing_label2 = tk.Label(self.master, text="OR", font=("Arial", 15, "bold"), bg="white")
        self.spacing_label2.pack(pady=10)
        self.expense_button = tk.Button(self.master, text="Expense", font=("Arial", 20, "bold"), command=lambda:sp.run(['python', 'NSB-AlgoProg-Group-Work/expenseinput.py']))
        self.expense_button.pack(pady=10)

if __name__ == "__main__":
    master = tk.Tk()
    app = EntryInput(master)
    master.mainloop()