# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = int(input('Введите число: '))
array = []
count = 0
start_element = 1
next_element = 2
while count < number:
    array.append(start_element)
    start_element = start_element * next_element
    count += 1
    next_element += 1
print(array)