from tkinter import ttk
import tkinter as tk
from time import sleep

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
# timer_reset = False

timer = None
long_break = None
work = None
short_break = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global  check_mark_canvas, canvas, reps, long_break
    # timer_reset = True

    reps = 0

    window.after_cancel(timer)
    # window.after_cancel(work)
    # window.after_cancel(short_break)

    canvas.itemconfig(clock_label, text='00:00')
    timer_label.config(text='Timer', foreground=GREEN)

    check_mark_canvas.destroy()
    check_mark_canvas = tk.Canvas(bg=YELLOW, highlightthickness=0)
    check_mark_canvas.grid(row=3 , column= 1)

    enable_button()


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps#, timer_reset
    global long_break, work, short_break
     

    # if timer_reset == True:
    #     return

    start_button.config(state='disabled')
    
    work_sec = 2 #WORK_MIN * 60
    short_break_sec = 1 #SHORT_BREAK_MIN * 60
    long_break_sec = 3 #LONG_BREAK_MIN *60

    # if reps == 0:
    #     check_mark_canvas.destroy()

    reps +=1


    if reps % 2 == 0:    
        ttk.Label(check_mark_canvas, text='✓', foreground=GREEN, background=YELLOW, font=(FONT_NAME, 18,'normal')).pack(side='left')

    # check_mark_label = ttk.Label(window, text='✓', foreground=GREEN, background=YELLOW, font=(FONT_NAME, 18,'normal'))
    

    if reps % 8 == 0:
        reps = 0
        count_down(long_break_sec, 'Long\nBreak', PINK)
        # long_break = window.after((long_break_sec + 1) * 1000, enable_button)

    elif reps % 2 == 1:
        count_down(work_sec, 'Work', RED )
        # work = window.after((work_sec + 1) * 1000, start_timer)
    
    elif reps % 2 == 0:
        count_down(short_break_sec, 'Break', GREEN)
        # short_break = window.after((short_break_sec + 1) * 1000, start_timer)


def enable_button():
    # global timer_reset
    start_button.config(state="normal")
    # timer_reset = False




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count, time_text, color_text):
    # global timer_reset

    # if timer_reset == True:
    #     count = 0

    timer_label.config(text=time_text, foreground=color_text)

    min = count // 60
    sec = count % 60
    
    if len(str(min)) == 1:
        min = f'0{min}'
    if len(str(sec)) == 1:
        sec = f'0{sec}'

    time = f'{min}:{sec}'

    canvas.itemconfig(clock_label, text=time)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1, time_text, color_text)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title('Pomodoro')
window.geometry('600x500')
window.config( bg = YELLOW)     #padx = 100, pady = 50,


window.columnconfigure(tuple(range(3)), weight=1, uniform='a')

window.rowconfigure(0, weight=4, uniform='a')
window.rowconfigure(1, weight=8, uniform='a')
window.rowconfigure(2, weight=1, uniform='a')
window.rowconfigure(3, weight=1, uniform='a')
window.rowconfigure(4, weight=2, uniform='a')

canvas = tk.Canvas(width = 200, height=223, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file = r'100 days of code\day 28\tomato.png')
canvas.create_image(100,112, image = tomato_img)
clock_label = canvas.create_text(100,130, text='00:00', fill = 'white', font = (FONT_NAME, 35, 'bold'))

check_mark_canvas = tk.Canvas(bg=YELLOW, highlightthickness=0)
check_mark_canvas.grid(row=3 , column= 1)




timer_label = ttk.Label(window, text='Timer', foreground=GREEN, background=YELLOW ,font = (FONT_NAME, 35, 'bold'))
start_button = ttk.Button(window, text='Start', command=start_timer)
reset_button =  ttk.Button(window, text='Reset', command=reset_timer)



canvas.grid(row=1, column=1, sticky='NEWS')

timer_label.grid(row=0, column=1, sticky='S')

start_button.grid(row=2, column=0, sticky='E')

reset_button.grid(row=2, column=2, sticky='W')




window.mainloop()