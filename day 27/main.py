import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.geometry('300x300')


# grid settings
root.columnconfigure(tuple(range(3)), weight=1, uniform='a')
# root.columnconfigure(3, weight=2, uniform='a')
root.rowconfigure(tuple(range(3)), weight = 1, uniform='a' )




ttk.Label(root, text='isso funciona?').grid(column=1, row=1, sticky='NEWS', padx=5, pady=5)




tk.mainloop()



