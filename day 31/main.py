import pandas as pd
from tkinter import ttk
import tkinter as tk
from time import sleep
from PIL import ImageTk, Image

BACKGROUND_COLOR = '#AADFC0'
CARD_BACK_PATH = r'100 days of code\day 31\images\card_back.png'
CARD_FRONT_PATH = r'100 days of code\day 31\images\card_front.png'
RIGHT_BUTTON_PATH = r'100 days of code\day 31\images\right.png'
WRONG_BUTTON_PATH = r'100 days of code\day 31\images\wrong.png'
CARD_FRONT_COLOR = '#FFFFFF'
CARD_BACK_COLOR = '#91C2AF'

# WORDS_DB_PATH = r'100 days of code\day 31\data\french_words.csv'


using_french_words_file = None
using_words_to_learn = None

try:
    load_db = pd.read_csv(r'100 days of code\day 31\data\words_to_learn.csv')
    using_words_to_learn = True    

except FileNotFoundError:
    load_db = pd.read_csv(r'100 days of code\day 31\data\french_words.csv')   
    using_french_words_file = True
# -------------------------- flash card turn function --------------------------
card_state =True

index =  0
def next_card(know = None):
    global index, card_state, load_db, id_event

    root.after_cancel(id_event)
    

    if know == False and using_french_words_file:
        try:
            df = pd.read_csv(r'100 days of code\day 31\data\words_to_learn.csv')
        except FileNotFoundError:
            column_names = ['French', 'English']
            df = pd.DataFrame(columns = column_names)


        new_row = {'French' : load_db.French[index], 'English' : load_db.English[index]}

        # if not any(df.isin(new_row.keys())):
        df = df.append(new_row, ignore_index = True)
        df.to_csv(r'100 days of code\day 31\data\words_to_learn.csv', index=False)


    if know == True and using_words_to_learn:
        load_db = load_db.drop(index).reset_index(drop=True)
        load_db.to_csv(r'100 days of code\day 31\data\words_to_learn.csv', index=False)
        
        index -= 1

    index += 1


    img_label.config(image=front_img)
    label_language.config(background=CARD_FRONT_COLOR, text=load_db.columns[0])
    label_word.config(background= CARD_FRONT_COLOR, text= load_db.French[index])
    card_state = False

    id_event = root.after(3000, flip_card)


def flip_card():
    global index
    img_label.config(image=back_img)
    label_language.config(background=CARD_BACK_COLOR, text=load_db.columns[1])
    label_word.config(background= CARD_BACK_COLOR, text= load_db.English[index])


# tkinter config
root = tk.Tk()
root.geometry('900x725')
root.config(background=BACKGROUND_COLOR, padx=50)


# grid config
root.columnconfigure((0,1),weight= 1, uniform='a')
root.rowconfigure((0), weight=1, uniform='a')
root.rowconfigure((1), weight=11, uniform='a')
root.rowconfigure((2), weight=3, uniform='a')


# imageTK
back_img = ImageTk.PhotoImage(Image.open(CARD_BACK_PATH))
front_img = ImageTk.PhotoImage(Image.open(CARD_FRONT_PATH))

wrong_img = ImageTk.PhotoImage(Image.open(WRONG_BUTTON_PATH))
right_img = ImageTk.PhotoImage(Image.open(RIGHT_BUTTON_PATH))


# widget + grid

img_label = tk.Label(root, image=front_img, background=BACKGROUND_COLOR)
img_label.grid(row=1, column=0, columnspan=2)

button_wrong = tk.Button(
                        root,
                        image=wrong_img,
                        highlightthickness=0,
                        bd=0,
                        command= lambda : next_card(know=False))

button_wrong.grid(row=2, column=1)


button_right = tk.Button(
                        root, 
                        image=right_img,
                        highlightthickness=0, 
                        bd=0,
                        command= lambda : next_card(know = True))

button_right.grid(row=2, column=0)

## labels + grid
label_language = tk.Label(text='French', font=('Ariel', 40, 'italic'), background=CARD_FRONT_COLOR)

label_word = tk.Label(text=f'{load_db["French"][index]}', font=('Ariel', 60, 'bold'), background=CARD_FRONT_COLOR)

label_language.place(x=400, y=150, anchor='center')
label_word.place(x=400, y=263, anchor='center')



id_event = root.after(3000, flip_card)


# run
root.mainloop()

