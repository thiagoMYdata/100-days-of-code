from tkinter import *
import requests


def get_quote():
    global quote_text
    response = requests.get(url=r'https://api.kanye.rest')
    ye_data = response.json()['quote']
    canvas.itemconfig(quote_text, text = ye_data)

window = Tk()
window.title("Ye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file=r"100 days of code\day 33\kanye-quotes\background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file=r"100 days of code\day 33\kanye-quotes\kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()