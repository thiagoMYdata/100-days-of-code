import smtplib
from random import choice
import datetime as dt 



now = dt.datetime.now()
my_email = 'appbreweryinfo@gmail.com'
password = 'vexnarxlphojwuzh'



if now.weekday() == 2:
    with open(r'100 days of code\day 32\quotes.txt') as file:
        quotes = file.read().split('\n')
        

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password= password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs='appbrewerytesting@yahoo.com',
            msg=f'Subject: Wednesday quote\n\n{choice(quotes)}'
        )

