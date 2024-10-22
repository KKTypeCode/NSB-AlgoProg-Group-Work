import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Entry Book")
text_var = tk.StringVar()
text_var.set("Digital Entry Book")

label = tk.Label(root, 
                 textvariable=text_var, 
                 anchor=tk.CENTER,      
                 height=3,              
                 width=25,                                
                 font=("Arial", 12, "bold"), 
                 fg="black",                            
                 justify=tk.CENTER,    
                 relief=tk.RAISED,                    
                )
label.pack(pady=10, padx= 10)
treeview = ttk.Treeview()
treeview = ttk.Treeview(columns=("name", "date", "ie", "value", "category", "delivered", "id"))
treeview.pack(pady=70, padx=30)
treeview.heading("#0", text="Index")
treeview.column("#0", width=50)
treeview.heading("name", text="Name")
treeview.heading("date", text="Date")
treeview.column("date", width=150)
treeview.heading("ie", text="Income/Expense")
treeview.column("ie", width=120)
treeview.heading("value", text="Value")
treeview.heading("category", text="Category")
treeview.heading("delivered", text="Delivered")
treeview.column("delivered", width=100)
treeview.heading("id", text="ID")
treeview.column("id", width=150)



label.pack(pady=20, padx= 20)
treeview.pack()
root.mainloop()