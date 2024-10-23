import tkinter as tk
from tkinter import *
import MainIO as io
from tkinter import messagebox

'''
def screenprnt():
    name = namestring.get()
    income = incomeint.get()
    date = dateint.get()
    rate = rateint.get()
    cat = catstring.get()
    complete1 = sel()
    print(name,income,date,rate,cat,complete1)
    namestring.set('')
    incomeint.set('')
    dateint.set('')
    rateint.set('')
    catstring.set('')
'''

def sel():
    complete = completionBool.get()
    return complete

def store_income():
        try:
            io.income(namestring.get(), dateint.get(), incomeint.get(), catstring.get(), completionBool.get())
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid inputs for all fields!")


root = tk.Tk()
root.geometry("900x600")

#Name Section
namestring=tk.StringVar()
namename = tk.Label(root, text = 'Input Name')
nameentry = tk.Entry(root, textvariable= namestring)
namename.pack(side = 'top',anchor = 'center', pady = 5)
nameentry.pack(side = 'top',anchor = 'center', pady = 5)

#Income Section
incomeint=tk.StringVar()
incomename = tk.Label(root, text = 'Input Income')
incomeentry = tk.Entry(root, textvariable= incomeint)
incomename.pack(side = 'top',anchor = 'center', pady = 5)
incomeentry.pack(side = 'top',anchor = 'center', pady = 5)

#Date Section
dateint=tk.StringVar()
datename = tk.Label(root, text = 'Input Date')
dateentry = tk.Entry(root, textvariable= dateint)
datename.pack(side = 'top',anchor = 'center', pady = 5)
dateentry.pack(side = 'top',anchor = 'center', pady = 5)

#Category Section
catstring=tk.StringVar()
catname = tk.Label(root, text = 'Input Category')
catentry = tk.Entry(root, textvariable= catstring)
catname.pack(side = 'top',anchor = 'center', pady = 5)
catentry.pack(side = 'top',anchor = 'center', pady = 5)

#Rate Section
rateint=tk.StringVar()
ratename = tk.Label(root, text = 'Input Rate/Date')
rateentry = tk.Entry(root, textvariable= rateint)
ratename.pack(side = 'top',anchor = 'center', pady = 5)
rateentry.pack(side = 'top',anchor = 'center', pady = 5)

#Completion of Transaction Section
completionBool=tk.BooleanVar()
completename = tk.Label(root, text = 'Input Completion of Transaction')
completename.pack(side = 'top',anchor = 'center', pady = 5)
R1 = Radiobutton(root, text='True',variable=completionBool, value=True, command=sel)
R1.pack(side = 'top',anchor = 'center', pady=5)
R2 = Radiobutton(root, text='False',variable=completionBool, value=False, command=sel)
R2.pack(side = 'top',anchor = 'center', pady=5)


#Button
button = tk.Button(root, text='Enter', command = store_income)
button.pack(side = 'top',anchor = 'center', pady = 5)

root.mainloop()

'''
Name 
Date 
Value/Income
Category 
Completion of Transaction t/f
'''