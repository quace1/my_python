import pandas as pd

url = "https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/football.csv"
football = pd.read_csv(url)

print(football.Age.mean()) #Task1

print(football.Composure.count()) #Task2

print(round(football.ShortPassing.std(), 2)) #Task3

print(football.Wage.sum()) #Task4

print(football.Value.min()) #Task5



