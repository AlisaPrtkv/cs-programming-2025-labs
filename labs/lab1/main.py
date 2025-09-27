#1
a = 24
b = 7.4
c = 'kek'
d = True
print('1.', a, b, c, d)

#2
name = 'Алиса'
age = 18
print('2.', name, age)

#3
i = 342
f = 56.2
s = '43'
p = i + f + int(s)
print('3.', p)

#4
a = 3
b = 8
r = (a + 4 * b) * (a - 3 * b) + a ** 2
print('4.', r)

#5
g = int(input())
n = int(input())
S = g * n
P = (g * 2) + (n * 2)
print('5.', S, P)

#6
print('6.''*   *   *')
print('   * * * * ')
print('    *   *  ')

#7, + - * // / % **, < > == <= >= !=
q = 15
w = 4
print('7.', q + w, q - w, q * w, q // w, q / w, q % w, q ** w)
print(q < w, q > w, q == w, q <= w, q >= w, q != w)

#8
print('8.',f'Привет, меня зовут {name}, мне {age} лет.')

#9 + строка, Съешь еще этих мягких французских булок, да выпей чаю
s = 'Съешь'
ee = 'ещё этих'
m = 'мягких'
f = 'французских'
b = 'булок'
d = 'да'
vch ='выпей чаю'
print('9.', s + ' ' + ee + ' ' + m + ' ' + f + ' ' + b + ', ' + d + ' ' + vch)

#10
st = 'Нет! Да!'
print('10.', (st + ' ') * 4)

#11
d = input()
ch, ch2, ch3 = d.split(', ')
print('11.', (int(ch) + int(ch3)) // int(ch2))

#12
s = 'подвыподверт'
print('12.', s[:4], s[10:], s[3:8], s[::-1])















