import pandas as pd

data = pd.read_csv(r'100 days of code\day 25\pandas\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
color_count = pd.DataFrame(data['Primary Fur Color'].value_counts())
print(color_count)