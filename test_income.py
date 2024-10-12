import tkinter as tk
from tkinter import *

root = tk.Tk()

def button_click():
    root.config(bg='white')
    print('Color Changed')

def button_black():
    root.config(bg='Black')
    print('Color Changed')

button = tk.Button(root, text='Change Color White', command=button_click)
button.pack(pady=10)
button = tk.Button(root, text='Change Color Black', command=button_black)
button.pack(pady=10)

root.title('Theme Changer')
root.geometry('1080x600')
root.mainloop()