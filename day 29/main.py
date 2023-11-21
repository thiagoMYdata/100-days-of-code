from tkinter import ttk
import tkinter as tk

window = tk.Tk()
window.geometry('600x700')

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

canvas = tk.Canvas(width = 400, height=400, bg='#fff', highlightthickness=0)
mypass_img = tk.PhotoImage(file = r'100 days of code\day 29\logo.png')
canvas.create_image(200,200, image = mypass_img)


canvas.pack(padx=20, pady=20,expand=True)



window.mainloop()