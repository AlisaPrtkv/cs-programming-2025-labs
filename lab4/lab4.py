#1
k = int(input("Введите температуру: "))
if k >= 20: print('Кондиционер включен')
else: print('Кондиционер выключен')

#2
m = int(input("Ведите номер месяца: "))
if m == 12 or m == 1 or m == 2: print('Зима')
elif 2 < m < 6: print('Весна')
elif 5 < m < 9: print('Лето')
elif 8 < m < 12: print('Осень')
else: print('Я сразу поняла, что ты змееносец')

#3
age = int(input("Введите собачие года: "))
if age < 1: print('Собака должна чуть-чуть прожить')
elif age > 22: print('Собаки столько не живут')
elif age * 1 != age: print('Возраст - это чиселки и циферки')
elif age == 1 or age == 2: print(age * 10.5)
else: print(21 + ((age - 2) * 4))

#4
ch = int(input("Введите число: "))
if int(str(ch)[-1]) % 2 == 0 and sum(map(int, str(ch))) % 3 == 0:
    print('Число делится на 6')
else: print('Число не делится на 6')

#5
pas = input("Введите пароль: ")
if len(pas) < 8: print('Пароль должен содержать не менее 8 символов')
if not any(c.isupper() for c in pas):
    print('Пароль должен содержать заглавные буквы')
if not any(c.islower() for c in pas):
    print('Пароль должен содержать строчные буквы')
if not any(c.isdigit() for c in pas):
    print('Пароль должен содержать цифры')
spec = "!@#$%^&*()_+-=[]{}|;:,.<>?~"
if not any(c in spec for c in pas):
    print('Пароль должен содержать специальные символы')
else: print('Да, всё классно, молодца')

#6
g = int(input("Введите год: "))
if (g % 4 == 0 and g % 100 != 0) or g % 400 == 0:
    print('Это високосный год')
else: print('Не високосный год')

#7
a = int(input("Введите число: "))
b = int(input("Введите число: "))
c = int(input("Введите число: "))
if a <= b and a <= c: smal = a
elif b <= a and b <= c: smal = b
else: smal = c
print(f"Наименьшее число: {smal}")

#8
sum = float(input("Введите сумму: "))
if sum < 1000: print(sum)
elif 1000 <= sum <= 5000: print(sum - ((sum * 5) / 100))
elif 5000 <= sum <= 10000: print(sum - ((sum * 10) / 100))
elif sum >= 10000: print(sum - ((sum * 15) / 100))
else: print('Ну чет не то, передумай')

#9
t = int(input('Введите время: '))
if 0 <= t <= 5: print('Ночь')
elif 6 <= t <= 11: print('Утро')
elif 12 <= t <= 17: print('День')
elif 18 <= t <= 23: print('Вечер')
else: print('В сутках только 24 часа')

#10
n = int(input("Введите число: "))
if n < 2: print('Не простое число')
elif n == 2: print('Простое число')
else:
    prost = True
if n % 2 == 0:
    prost = False
    print('Составное число')
else:
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            prost = False
            print('Составное число')
            break
    if prost:
        print('Простое число')







