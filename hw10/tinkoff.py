import pandas as pd
import json

#Task1
url = "https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/tinkoff_hh.json"
with open('data.txt', encoding='utf8') as data:
    file = data.readlines()
database = [json.loads(element) for element in file if 'index' not in element]
df = pd.DataFrame(database)
dfVacancyIncome = df[["vacancy","income","region"]][df["income"] != "не указан"].drop_duplicates()
dfVacancyIncome['vacancy'] = dfVacancyIncome['vacancy'].str.lower()
dfVacancyIncome = dfVacancyIncome.drop_duplicates()
print(dfVacancyIncome["vacancy"].value_counts())

