path = r'100 days of code\day 25\pandas\weather_data.csv'

# with open(path, mode='r') as file:
#     file_list =   file.readlines()
#     print(file_list)

# import csv

# with open(path) as file:
#     data = list(csv.reader(file))
#     temperatures = []
#     for row in data[1:]:
#         temperatures.append(int(row[1]))

# print(temperatures) 

import pandas as pd
data = pd.read_csv(path)
print(data['temp'])