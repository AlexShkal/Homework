# Выведите n-ое число Фибоначчи, используя только временные переменные,
# циклические операторы и условные операторы. n - вводится.

n = int(input('Введите номер числа Фибоначчи '))


def fibonacci_number(value: int):
    first = 0
    second = 1

    if value == 1:
        return print(f"Первое число Фибоначчи  {first}")

    elif value == 2:
        return print(f"Второе число Фибоначчи  {second}")

    for _ in range(2, value):
        temp = second
        second = first + second
        first = temp
    return print(f" {value} число Фибоначчи  {second}")

# Определите, является ли число палиндромом (читается слева направо и справа налево одинаково)
# Число положительное целое, произвольной длины.
# Задача требует работать только с числами (без конвертации числа в строку или что-нибудь еще).
n = int(input())
n1 = n
m = 0
while n != 0:
    i = n % 10
    m = m * 10 + i
    n = n // 10
if m == n1:
    print('Полиндром')
else:
    print('Не является полиндромом')

# Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел, кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz,
# а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz.
for num in range(1, 101):
    fizz = num % 3 == 0
    buzz = num % 5 == 0

    if fizz and buzz:
        print("FizzBuzz")
    elif fizz:
        print("Fizz")
    elif buzz:
        print("Buzz")
    else:
        print(num)