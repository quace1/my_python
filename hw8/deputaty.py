import pandas as pd
from datetime import datetime, timedelta

url = "https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/deputat.csv"
df = pd.read_csv(url)
df['datetime_birthdate'] = df.apply(lambda row: datetime.strptime(row['birthdate'], '%d.%M.%Y'), axis = 1)
df['age'] = df.apply(lambda row: pd.Timedelta(datetime.now() - row['datetime_birthdate']).days/365.25, axis = 1)
print(round(df['age'].mean()))#средний возраст
df['gender'].value_counts()
print(str(round(179*100/211))+'% - мужчины')
print(str(round(32*100/211))+'% - женщины')