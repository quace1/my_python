from datetime import datetime, timedelta

date = 'May 9 2017 9:00AM'
s = datetime.strptime(date, '%b %d %Y %H:%M%p')
print(s) #Task1

s += timedelta(hours = 1)
print(s) #Task2

print(s.strftime('%Y-%m-%d')) #Task3

startDate = '2020-01-01 00:00' #Task4
endDate = '2020-01-04 00:00'
startDate = datetime.strptime(startDate, '%Y-%m-%d %H:%M')
endDate = datetime.strptime(endDate, '%Y-%m-%d %H:%M')
curDate = startDate
while curDate != endDate:
    print(curDate)
    curDate += timedelta(hours = 1)






