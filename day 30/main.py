from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import pandas as pd
from password_builder import builder
import pyperclip # <---
import json

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
FILE_PATH = r'100 days of code\day 30\mypasswordfile.json'


# ---------------------------- PASSWORD GENERATOR ------------------------------- # 

def password_generator():

    password = builder()

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)



def password_configurate(): #passivel de exclusao
    window_config = tk.Toplevel()


    window_config.columnconfigure(0, weight=2, uniform='a')
    window_config.columnconfigure(1, weight=1, uniform='a')
    window_config.rowconfigure((0,1,2), weight=1, uniform='a')


    ttk.Label(window_config, text='nº characters:').grid(column=0, row=0, sticky='e', padx=10,pady=2)
    ttk.Label(window_config, text='nº numbers:').grid(column=0, row=1, sticky='e', padx=10,pady=2)
    ttk.Label(window_config, text='nº special characters:').grid(column=0, row=2, sticky='e', padx=10,pady=2)

    char_var = tk.StringVar()
    num_var = tk.StringVar()
    spec_char_var = tk.StringVar()

    char_var.set('6')
    # num_var.set('2')
    spec_char_var.set('1')

    character_entry = ttk.Entry(window_config, textvariable=char_var, width=10)
    character_entry.grid(column=1, row=0)
    # character_entry.insert(0, '3243432432424234f')

    numbers_entry = ttk.Entry(window_config, textvariable=num_var, width=10)
    numbers_entry.grid(column=1, row=1)
    # numbers_entry.insert(0,'2')

    special_charac_entry = ttk.Entry(window_config, textvariable=spec_char_var, width=10)
    special_charac_entry.grid(column=1, row=2)
    # special_charac_entry.insert(0,'1')

    # result = [int(char_var.get()), int(num_var.get()), int(spec_char_var.get())]

    # return result



# ---------------------------- SAVE PASSWORD ------------------------------- # 

def get_info():
    # get web email_user password
    web = web_var.get()
    email_user = email_user_var.get()
    password = password_var.get()


    if web != '' and password != '' and email_user != '': 

        password_save(web=web, email_user=email_user, password=password)
    
    else:
        messagebox.showwarning(title='Fill everything', message='Dont leave empty entry behind')


def password_save(web, email_user, password):
    # try:
    #     pd.read_json(path_or_buf=file_path)    
    # except Exception:
    #     pass
    #     #site, email or username, password
    #     # data = {'site':[], 'email or username':[], 'password':[]}
    #     # df = pd.DataFrame(data)

    #     data = pd.DataFrame(columns=['site', 'email or username', 'password'])
    #     data.to_json(path_or_buf=file_path, orient='table')

    # finally:
    #             data = pd.read_json(file_path,orient='table')
    
    # mask = (data['site'] == web) & (data['email or username'] == email_user) & (data['password']  == password)

    # if not any(mask):
    is_ok = messagebox.askokcancel(title='Info confirmation', message=f'[*] Web:\n{web}\n\n[*] Email or user:\n {email_user}\n\n[*] Password:\n{password}')
    
    if is_ok:
    
        new_row = {
            web : {
            'email or username':email_user,
            'password':password}
            }
        # data = data.append(new_row, ignore_index=True)
        # data.to_json(file_path, orient='split')


        try:
            with open(FILE_PATH,'r'):
                pass
        except FileNotFoundError:
            with open(FILE_PATH, 'w') as data_file:
                json.dump(new_row, data_file, indent=4)
        else:
            with open(FILE_PATH,'r') as data_file:
                # reading old data
                data_load = json.load(data_file) # [^_^] iqual to read_json
                # updating old data with new data
                data_load.update(new_row)

                print(data_load)
                print(type(data_load))
  

            with open(FILE_PATH, 'w') as data_file:
                json.dump(data_load, data_file, indent=4) #[^_^] dump( text, file path, dict scoop config)

        website_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)

    else:
        messagebox.showinfo(title='Can\'t save', message='This info already been saved before') #i think this is wrong 

# ---------------------------- FIND PASSWORD ------------------------------- # 


def search_password():
    web = web_var.get()

    if not (web == ''):

        try:
            with open(FILE_PATH, 'r') as data_file:
                data_load = json.load(data_file)
                email = data_load[web]["email or username"]
                password = data_load[web]['password']

                messagebox.showinfo(title=web.center(100), message=f'Email or user: {email}\nPassword: {password}')

        except KeyError:
            messagebox.showerror(message='Website not found. Try again!')

        except FileNotFoundError:
            messagebox.showerror(message='No Data File Found.')

# ---------------------------- UI SETUP ------------------------------- #
#canvas
canvas = tk.Canvas(width = 200, height=200, bg='#fff', highlightthickness=0)
mypass_img = tk.PhotoImage(file = r'100 days of code\day 30\logo.png')
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
email_username_label = ttk.Label(grid_frame, text='Login: ', background='#fff')
password_label = ttk.Label(grid_frame, text= 'Password: ', background='#fff')

# entry create
website_entry = ttk.Entry(grid_frame, width=55, textvariable=web_var)
website_entry.focus() # focus()
email_username_entry = ttk.Entry(grid_frame, width=55, textvariable=email_user_var)
email_username_entry.insert(0, 'youremail@gmail.com') # insert() 
password_entry = ttk.Entry(grid_frame, width=41, textvariable=password_var)

# button create
password_button = ttk.Button(grid_frame, text='Generate Password', width=25, command=password_generator)
add_button = ttk.Button(grid_frame, text='Add', width=55, command=get_info)
search_button = ttk.Button(grid_frame, text='Search', width=25, command=search_password)

# label grid
website_label.grid(row=0, column=0, sticky='e', padx=5)
email_username_label.grid(row=1, column=0, sticky='e', padx=5)
password_label.grid(row=2, column=0, sticky='e', padx=5)

# entry grid
website_entry.grid(row=0, column=1, sticky='w')
email_username_entry.grid(row=1, column=1, columnspan=3, sticky='w')
password_entry.grid(row=2, column=1, sticky='w')

# button grid
password_button.grid(row=2, column=2, sticky='e')
add_button.grid(row=3, column=1,columnspan=2, sticky='w',pady=2)
search_button.grid(row=0, column=2, sticky='e' )


# run
window.mainloop()