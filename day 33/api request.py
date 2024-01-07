import requests
import datetime as dt
import smtplib

## REQUESTS API
response = requests.get(url=r'http://api.open-notify.org/iss-now.json')
response.raise_for_status()
iss_longitude = float(response.json()['iss_position']['longitude'])
iss_latitude = float(response.json()['iss_position']['latitude'])

# iss_position_data = (longitude, latitude)
# print(iss_position_data)


## REQUESTS API WITH PARAMETERS
# parameters = {'lat':-23.947421, 'lng': -23.947421, 'formatted' : 0}
# response =  requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)


lat = -23.948119
lng = -46.366963

if (lat + 5) >= iss_latitude >= (lat - 5) and (lng + 5) >= iss_longitude >= (lng - 5):
    my_email = 'appbreweryinfo@gmail.com'
    password = 'vexnarxlphojwuzh'       

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password= password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs='appbrewerytesting@yahoo.com',
            msg=f'Subject: Yooo look up at the sky the ISS is near u\n\n Rare opportunity to look at the sky and try to see the ISS. There is no much to look without a telescope anyways baj baj '
        )




# data = response.json()
# sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
# sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])
# print(sunrise, sunset)

# time_now = dt.datetime.now()
# print(time_now.hour)