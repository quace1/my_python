import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/it.csv')
dfRub = df[df['З/п в валюте найма'].str.contains('₽')]
meanWage = dfRub['З/п в валюте найма'].str.translate(str.maketrans({'₽': '', ',': '.', u'\xa0': ''})).astype(float).mean()
print(str(meanWage) + '₽') #средняя з.п. в рублях
print(dfRub.groupby(['Технология'])['З/п в валюте найма'].max())#технология с макс з.п.
print(dfRub.groupby(['Дата рождения'])['З/п в валюте найма'].max())#возрастп программистов с максимальной з.п.
print(df[df['Вакансия'].str.contains('Engineer')][['Вакансия','З/п в валюте найма']])#з.п. работников со словом Engineer в вакансии
