import random

a = ['самовар', 'весна', 'лето']

s = a[random.randint(0, len(a)-1)]

x = random.randint(0, len(s)-1)

if x == 0:
    s1 = '?' + s[1:]
elif x == len(a)-1:
    s1 = s[0:len(a)-1] + '?'
else:
    s1 = s[0:x-1] + '?' + s[x:]

print(s1)

l = str(input('Введите букву:'))

if l == s[x-1]:
    print('Победа!')
    print('Слово:', s)
else:
    print('Увы! Попробуйте в другой раз.')
    print('Слово:', s)
