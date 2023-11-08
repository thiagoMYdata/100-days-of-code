import tkinter as tk
import ttkbootstrap as ttk


def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result_label.config(text=str(km))

root = ttk.Window(themename='solar')
root.title('Miles to Kilometer Converter')
root.config(padx=20, pady=20)



miles_input = ttk.Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = ttk.Label(text='Miles')
miles_label.grid(column=2, row=0)

is_equal_label = ttk.Label(text='Is equal to')
is_equal_label.grid(column=0, row=1)

kilometer_result_label = ttk.Label(text='0')
kilometer_result_label.grid(column=1, row=1)

kilometer_label = ttk.Label(text='km')
kilometer_label.grid(column=2, row=1)

calculate_button = ttk.Button(text='Calculate', command=miles_to_km)
calculate_button.grid(column=1, row=2)

root.mainloop()