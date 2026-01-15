#1
def convert_time_string(input_str):
    parts = input_str.split()
    if len(parts) != 3:
        raise ValueError("Некорректный формат ввода.")
    value_str, from_unit, to_unit = parts
    try:
        value = float(value_str)
    except ValueError:
        raise ValueError(f"Некорректное числовое значение: {value_str}")
    def convert_units(val, from_u, to_u):
        if from_u == 's':
            in_seconds = val
        elif from_u == 'm':
            in_seconds = val * 60
        elif from_u == 'h':
            in_seconds = val * 3600
        else:
            raise ValueError(f"Неподдерживаемая единица измерения: {from_u}")
        if to_u == 's':
            return in_seconds
        elif to_u == 'm':
            return in_seconds / 60
        elif to_u == 'h':
            return in_seconds / 3600
        else:
            raise ValueError(f"Неподдерживаемая единица измерения: {to_u}")
    result = convert_units(value, from_unit, to_unit)
    if result.is_integer():
        return f"{int(result)}{to_unit}"
    else:
        return f"{round(result, 2)}{to_unit}"
def main():
    print("Конвертер времени")
    print("Примеры ввода: '4 h m', '30 m h', '12 s h'")
    print("Поддерживаемые единицы: s (секунды), m (минуты), h (часы)")
    print("Введите 'выход' для завершения")
    print("-" * 40)
    while True:
        user_input = input("\nВведите значение для конвертации: ").strip()
        if user_input.lower() in ['выход', 'exit', 'quit', 'q']:
            print("Программа завершена.")
            break
        if not user_input:
            print("Пожалуйста, введите данные.")
            continue
        try:
            result = convert_time_string(user_input)
            print(f"Результат: {result}")
        except ValueError as e:
            print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Неожиданная ошибка: {e}")
if __name__ == "__main__":
    main()

#2
def calculate_profit(a, n):
    if a < 30000:
        return 0
    bonus = min((a // 10000) * 0.3, 5)
    if n <= 3:
        rate = 3
    elif n <= 6:
        rate = 5
    else:
        rate = 2
    rate += bonus
    total = a
    for _ in range(n):
        total *= (1 + rate / 100)
    return round(total - a, 2)

a = int(input("Сумма вклада (руб.): "))
n = int(input("Срок (лет): "))
print(f"Прибыль: {calculate_profit(a, n)} руб.")

#3
def quick_primes():
    try:
        s, e = map(int, input("Диапазон: ").split())
        if s > e: print("Error!"); return
        primes = [n for n in range(s, e + 1)
                  if n >= 2 and all(n % i != 0
                                    for i in range(2, int(n ** 0.5) + 1))]
        print(" ".join(map(str, primes)) if primes else "Error!")
    except:
        print("Error!")
quick_primes()

#4
def matrix_addition_simple():
    try:
        n = int(input())
        if n <= 2:
            print("Error!")
            return
        m1 = []
        for _ in range(n):
            row = list(map(float, input().split()))
            if len(row) != n:
                print("Error!")
                return
            m1.append(row)
        m2 = []
        for _ in range(n):
            row = list(map(float, input().split()))
            if len(row) != n:
                print("Error!")
                return
            m2.append(row)
        for i in range(n):
            row_result = []
            for j in range(n):
                row_result.append(str(m1[i][j] + m2[i][j]))
            print(" ".join(row_result))
    except:
        print("Error!")
if __name__ == "__main__":
    print("=== Сложение матриц ===")
    print("Введите:")
    print("1. Размер матрицы n (n > 2)")
    print("2. Первую матрицу (n строк по n чисел)")
    print("3. Вторую матрицу (n строк по n чисел)")
    print()
matrix_addition_simple()

#5
def is_palindrome(text):
    cleaned = ''.join(ch.lower() for ch in text if ch.isalnum())

    return cleaned == cleaned[::-1]
def check_palindrome():
    text = input("Введите строку: ")
    result = is_palindrome(text)
    print("Да" if result else "Нет")
check_palindrome()
