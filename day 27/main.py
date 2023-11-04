import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.geometry('300x200')


# grid settings
root.columnconfigure(tuple(range(3)), weight=1, uniform='a')


# root.columnconfigure(3, weight=2, uniform='a')
root.rowconfigure(tuple(range(3)), weight = 1, uniform='a' )

root.rowconfigure(0, weight=3, uniform='a')

root.rowconfigure(2, weight=3, uniform='a')

number =  tk.DoubleVar(value=0)

def numfunc():
    value = number.get()
    miles = value* 1.60934
    number =  tk.DoubleVar()
    return number

    #  tk.IntVar(float(value) *)
    # return number


# def numfunc():
#     value = number.get()
#     miles = value * 0.621371  # Conversão de quilômetros para milhas
#     return   # Retorna o valor formatado para exibir nas labels

def update_label():
    miles = numfunc()
    label_miles.config(text=miles)




ttk.Label(root, text='Is equal to', anchor='e',background='#555').grid(column=0, row=1, sticky='NEWS', padx=5)

ttk.Label(root, text='0', anchor='center',background='#666', textvariable=lambda :numfunc() ).grid(column=1, row=1, sticky='NEWS', pady=5)

ttk.Label(root, text='km', anchor='w', background='#444').grid(column=2, row=1, sticky='NEWS', pady=5)

ttk.Entry(root, textvariable=lambda: numfunc()).grid(column=1, row=0, sticky='s', pady=5)

ttk.Label(root, text='Miles', anchor='sw', background='#444').grid(column=2, row=0, sticky='NEWS', pady=5)


tk.mainloop()

# eu tinha que fazer alguma edicao pra manter a streak..

