import tkinter as tk

def screenprnt():
    income = incomeint.get()
    print(income)
    incomeint.set('')

root = tk.Tk()
root.geometry("900x600")

incomeint=tk.StringVar()

incomename = tk.Label(root, text = 'Input income')
incomeentry = tk.Entry(root, textvariable= incomeint)
button = tk.Button(root, text='Enter', command = screenprnt)

widthW = root.winfo_width()
widthname = incomename.winfo_width()
widthentry = incomeentry.winfo_width()
widthbutton = button.winfo_width()

x = (widthW - widthname) // 2

incomename.pack(side = 'top',anchor = 'center', pady = 10)
incomeentry.pack(side = 'top',anchor = 'center', pady = 10)
button.pack(side = 'top',anchor = 'center', pady = 10)

root.mainloop()