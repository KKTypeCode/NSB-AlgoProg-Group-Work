import tkinter as tk

root=tk.Tk()
root.geometry("500x300")
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=4)
root.title(string="Finance")
root.configure()


FinanceName_entry = tk.Entry(root)
FinanceName_entry.grid(column=1, row=0, sticky="EW", padx= 5, pady =5)

#username button
username_label = tk.Label(root, text="FINANCE", font=("Arial", 20))
username_label.grid(column=0, row=0, sticky=tk.W, padx= 5, pady= 5)


#password
password_label = tk.Label(root, text="Password:")
password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

password_entry = tk.Entry(root, show="*")
password_entry.grid(column=1, row=1, sticky="EW", padx=5, pady=5)

# login button
login_button = tk.Button(root, text="Login",command=lambda:print("pressed"))
login_button.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)

# registration button
registration_button = tk.Button(root, text="Register",command=lambda:print("pressed"))
registration_button.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)

# forgot button
forgot_button = tk.Button(root, text="Forgot Password",command=lambda:print("pressed"))
forgot_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

root.mainloop()