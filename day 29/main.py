from tkinter import ttk
import tkinter as tk
import pandas as pd


window = tk.Tk()
window.config(pady=20,background='#fff')
window.maxsize(500,400)

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- PASSWORD GENERATOR ------------------------------- # 


# ---------------------------- SAVE PASSWORD ------------------------------- # 

def get_info():
    # get web email_user password
    web = web_var.get()
    email_user = email_user_var.get()
    password = password_var.get()

    password_save(web=web, email_user=email_user, password=password)


def password_save(web, email_user, password):
    try:
        pd.read_csv(r'100 days of code\day 29\mypasswordfile.csv')    
    except FileNotFoundError:    
        #site, email or username, password
        data = {'site':[], 'email or username':[], 'password':[]}
        df = pd.DataFrame(data)
        df.to_csv(r'100 days of code\day 29\mypasswordfile.csv', index=False)

    data = pd.read_csv(r'100 days of code\day 29\mypasswordfile.csv')

    mask = (data['site'] == web) & (data['email or username'] == email_user) & (data['password']  == password)

    print(any(mask))

    if not any(mask):
        new_row = {'site':web, 'email or username':email_user, 'password':password}

        data = data.append(new_row, ignore_index=True)

        data.to_csv(r'100 days of code\day 29\mypasswordfile.csv', index=False)


# ---------------------------- UI SETUP ------------------------------- #
#canvas
canvas = tk.Canvas(width = 200, height=200, bg='#fff', highlightthickness=0)
mypass_img = tk.PhotoImage(file = r'100 days of code\day 29\logo.png')
canvas.create_image(100,100, image = mypass_img)
canvas.pack(expand=True)
# grid_frame
grid_frame = tk.Frame(window,background='#fff')
grid_frame.pack(expand=True, padx=40, fill='both')

# grid configure
grid_frame.columnconfigure(tuple(range(3)),weight=2 ,uniform='a')
grid_frame.columnconfigure(0, weight=1, uniform='a')

grid_frame.rowconfigure(tuple(range(4)), uniform='a')


# tkinter var
web_var = tk.StringVar()
email_user_var = tk.StringVar()
password_var = tk.StringVar()


# label create
website_label = ttk.Label(grid_frame, text='Website: ', background='#fff')
email_username_label = ttk.Label(grid_frame, text='Email/Username: ', background='#fff')
password_label = ttk.Label(grid_frame, text= 'Password: ', background='#fff')

# entry create
website_entry = ttk.Entry(grid_frame, width=55, textvariable=web_var)
website_entry.focus() # focus()
email_username_entry = ttk.Entry(grid_frame, width=55, textvariable=email_user_var)
email_username_entry.insert(0, 'youremail@gmail.com') # insert() 
password_entry = ttk.Entry(grid_frame, width=41, textvariable=password_var)

# button create
password_button = ttk.Button(grid_frame, text='Generate Password', width=25)
add_button = ttk.Button(grid_frame, text='Add', width=55, command=get_info)

# label grid
website_label.grid(row=0, column=0, sticky='e', padx=5)
email_username_label.grid(row=1, column=0, sticky='e', padx=5)
password_label.grid(row=2, column=0, sticky='e', padx=5)

# entry grid
website_entry.grid(row=0, column=1, columnspan=3, sticky='w')
email_username_entry.grid(row=1, column=1, columnspan=3, sticky='w')
password_entry.grid(row=2, column=1, sticky='w')

# button grid
password_button.grid(row=2, column=2, sticky='e')
add_button.grid(row=3, column=1,columnspan=2, sticky='w',pady=2)


# run
window.mainloop()