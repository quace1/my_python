import pandas as pd
from datetime import datetime
df = pd.read_csv("https://raw.githubusercontent.com/dm-fedorov/python_basic/master/data/vkontakte_group_01_2016-08-01_2020-03-15.csv")

def change_datetime(row):
  return datetime.strptime(row['Дата'], '%d.%m.%Y')

#Task1
dfСriterion = pd.get_dummies(df, columns = ['Критерий'])
viewersDates = dfСriterion[['Дата', 'Значение']][dfСriterion['Критерий_views'] == 1]
viewersDates['Дата'] = viewersDates.apply(change_datetime, axis = 1)
print(viewersDates.head())
viewersDates['Дата'] = viewersDates['Дата'].dt.strftime('%Y')
seriesViwersPerYear = viewersDates.groupby(['Дата'])['Значение'].sum()

#Task2
audienceReach = dfСriterion[['Дата','Значение']][dfСriterion['Критерий_reach'] == 1]
audienceReach['Дата'] = audienceReach.apply(change_datetime, axis = 1)
seriesReachPerMonth = audienceReach.groupby(['Дата'])['Значение'].sum()
audienceReachSubscribers = dfСriterion[['Дата','Значение']][dfСriterion['Критерий_reach_subscribers'] == 1]
audienceReachSubscribers['Дата'] = audienceReachSubscribers.apply(convert_to_datetime, axis = 1)
audienceReachSubscribers['Дата'] = audienceReachSubscribers['Дата'].dt.strftime('%Y-%m')
seriesReachSubscribersPerMonth = audienceReachSubscribers.groupby(['Дата'])['Значение'].sum()

#Task3
genderData = dfСriterion[['Дата', 'Значение','Парам. №1']][dfСriterion['Критерий_gender'] == 1]
genderSeries = genderData.groupby(['Парам. №1'])['Значение'].sum()
population = 10063 + 12637
male = 'Мужчины: ' + str(round(12637 * 100 / population)) + '%'
female = 'Женщины: ' + str(round(10063 * 100 / population)) + '%'
ageData = dfСriterion[['Парам. №1', 'Значение']][dfСriterion['Критерий_age'] == 1]
ageSeries = ageData.groupby(['Парам. №1'])['Значение'].sum()
countryData = dfСriterion[['Парам. №1','Значение']][dfСriterion['Критерий_countries'] == 1]
countrySeries = countryData.groupby(['Парам. №1'])['Значение'].sum()

#Task4
feedbackData = dfСriterion[['Дата','Парам. №1','Значение']][dfСriterion['Критерий_feedback'] == 1]
feedbackData['Дата'] = feedbackData.apply(change_datetime, axis = 1)
feedbackData['Дата'] = feedbackData['Дата'].dt.strftime('%Y-%m')
feedbackData['Парам. №1'].value_counts()
feedbackLike = feedbackData[feedbackData['Парам. №1'] == 'Нравится']
seriesFeedbackLike = feedbackLike.groupby(['Дата'])['Значение'].sum()