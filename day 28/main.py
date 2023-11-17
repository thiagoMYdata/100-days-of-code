from tkinter import ttk
import tkinter as tk

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
window = tk.Tk()
window.title('Pomodoro')
window.config( bg = YELLOW)     #padx = 100, pady = 50,

canvas = tk.Canvas(width = 200, height=223, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file = r'100 days of code\day 28\tomato.png')
canvas.create_image(100,112, image = tomato_img)
canvas.create_text(100,130, text='00:00', fill = 'white', font = (FONT_NAME, 35, 'bold'))



timer_label = ttk.Label(window, text='Timer', foreground=GREEN, background=YELLOW ,font = (FONT_NAME, 35, 'bold'))

start_button = ttk.Button(window, text='Start')

reset_button =  ttk.Button(window, text='Reset')

window.columnconfigure(tuple(range(3)), weight=1, uniform='a')

window.rowconfigure(0, weight=4, uniform='a')
window.rowconfigure(1, weight=8, uniform='a')
window.rowconfigure(2, weight=1, uniform='a')
window.rowconfigure(3, weight=1, uniform='a')
window.rowconfigure(4, weight=2, uniform='a')


canvas.grid(row=1, column=1, sticky='NEWS')

timer_label.grid(row=0, column=1, sticky='S')

start_button.grid(row=2, column=0, sticky='E')

reset_button.grid(row=2, column=2, sticky='W')

check_mark = '✅︎'


window.mainloop()