#1
name = input()
age = input()
for i in range(10):
    print(f"{i + 1}. Меня зовут {name} и мне {age} лет.")
#2
a = int(input())
for i in range(11):
    print(a * i)

#3
for i in range(0, 101, 3):
    print(i)

#4
n = int(input())
if n < 0:
    print("no no no")
else:
    f = 1
    i = 1
    while i <= n:
        f *= i
        i += 1
    print(f)

#5
b = 21
while b > 0:
    b -= 1
    print(b)

#6
d = int(input())
a, b = 0, 1
while a <= d:
    print(a, end=" ")
    a, b = b, a + b

#7
t = input()
r = ''
for i in range(len(t)):
    r += t[i] + str(i + 1)
print(r)

#8
while True:
    g = input()
    if g.lower() == 'q':
        break
    n = g.split()
    if len(n) == 2:
        try:
            n1 = float(n[0])
            n2 = float(n[1])
            res = n1 + n2
            print(f"Sum: {res}")
        except ValueError:
            print("Err")
    else:
        print("Err")
    print()
