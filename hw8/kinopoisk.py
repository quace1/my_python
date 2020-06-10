import pandas as pd

url = "https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/new_year_film.csv"
data = pd.read_csv(url)
print(data['ranking'].str.replace(',','.').astype(float).mean())