import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Transaction History")
text_var = tk.StringVar()
text_var.set("Transaction History")

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
treeview = ttk.Treeview()
treeview = ttk.Treeview(columns=("date", "transaction"))
treeview.heading("#0", text="No.")
treeview.heading("date", text="Date")
treeview.heading("transaction", text="Transaction")

label.pack(pady=20)
treeview.pack()
root.mainloop()