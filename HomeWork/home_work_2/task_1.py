# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

number = (input('Введите вещественное число: '))
sum_digits = 0
for digit in number:
    if digit.isdigit():
        sum_digits += int(digit)  
print(f'Сумма цифр данного числа = {sum_digits}')