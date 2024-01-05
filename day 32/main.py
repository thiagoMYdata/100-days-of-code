##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import pandas as pd
import datetime as dt
import smtplib



my_email = 'appbreweryinfo@gmail.com'
password = 'vexnarxlphojwuzh'


now = dt.datetime.now()

birthdays_db = pd.read_csv(r'100 days of code\day 32\birthdays.csv')


path_name = r'100 days of code\day 32\letter_templates'
letters_paths = [path_name + r'\letter_1.txt', path_name + r'\letter_2.txt', path_name + r'\letter_3.txt']


for i in range(len(birthdays_db)):
    # print(birthdays_db.iloc[i,2:4])
    row = birthdays_db.iloc[i]
    this_bday = dt.datetime(year=row.year, month=row.month, day=row.day)

    if this_bday.month == now.month and this_bday.day == now.day:
        with open(r'100 days of code\day 32\quotes.txt') as file:
            quotes = file.read().split('\n')
        with open(letters_paths[i]) as file:
            letter = file.read().replace('[NAME]', row['name'])

        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password= password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=row.email,
                msg=f'Subject: Your B day :)\n\n{letter}'
            )





