from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

START_URL = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
page = requests.get(START_URL)
soup = bs(page.text, 'html.parser')
table = soup.find_all('table')
star_data = []
table_rows = table[7].find_all('tr')

for rows in table_rows:
    td = rows.find_all('td')
    row = [i.text.rstrip() for i in td]
    star_data.append(row)

star_name = []
distance = []
mass = []
radius = []

for i in range(1, len(star_data)):
    star_name.append(star_data[i][0])
    distance.append(star_data[i][5])
    mass.append(star_data[i][8])
    radius.append(star_data[i][9])

df = pd.DataFrame(list(zip(star_name, distance, mass, radius)), columns=['star_name', 'distance', 'mass', 'radius'])
print(df)
df.to_csv('dwarf_stars.csv')