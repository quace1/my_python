file = open('temper.stat.txt', 'r')
sum = 0
cnt = 0
min = 1000
max = -1000

for line in file:
    sum += float(line)
    cnt += 1
    if float(line) > max:
        max = float(line)
    if float(line) < min:
        min = float(line)

print(min, max, sum/cnt)