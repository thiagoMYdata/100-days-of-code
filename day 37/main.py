import requests
from datetime import datetime as dt

USERNAME = 'goodonelule'
TOKEN = 'yhtfiosuawkmfyhgtglsguautyasetmyopEE'
GRAPH_ID = 'reading-streak'
pixela_endpoint = 'https://pixe.la/v1/users'

# user_params = {
#     'token': TOKEN,
#     'username': USERNAME,
#     'agreeTermsOfService':'yes',
#     'notMinor':'yes'
# }

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

# graph_config ={
#     'id' : 'reading-streak',
#     'name' : 'daily reading challenge',
#     'unit' : 'Pages',
#     'type' : 'int',
#     'color' : 'shibafu'
# }

headers = {
    'X-USER-TOKEN':TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


pixel_creation_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'


today = dt.now()

pixel_data = {
    'date' : today.strftime('%Y%m%d'),
    'quantity' : 'n_pages'
}


# response = requests.post(url=graph_endpoint, json=pixel_data, headers=headers)
# print(response.text)

