import pandas as pd

url = "https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/football.csv"
football = pd.read_csv(url)

print(round(football[football.Wage > football.Wage.mean()].SprintSpeed.mean(), 2)) #Task1

print(round(football[football.Wage < football.Wage.mean()].SprintSpeed.mean(), 2)) #Task2

print(football[football.Wage == football.Wage.max()].Position.sum()) #Task3

print(football[football.Nationality == 'Brazil'].Penalties.sum()) #Task4

print(round(football[football.HeadingAccuracy > 50].Age.mean(), 2)) #Task5

print(football[(football.Composure > 0.9*football.Composure.max()) & (football.Reactions > 0.9*football.Reactions.max())].Age.min()) #Task6

print(round(football[football.Age == football.Age.max()].Reactions.mean()-football[football.Age == football.Age.min()].Reactions.mean()), 2) #Task7

print(football[football.Value > football.Value.mean()].Nationality.max()) #Task8

print(round(football[(football.Position == 'GK') & (football.GKReflexes == football.GKReflexes.max())].Wage.mean() / football[(football.Position == 'GK') & (football.GKHandling == football.GKHandling.max())].Wage.mean(), 2)) #Task9

print(round(football[football.Aggression == football.Aggression.max()].ShotPower.sum() / football[football.Aggression == football.Aggression.min()].ShotPower.sum(), 2)) #Task10

