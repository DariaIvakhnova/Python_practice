# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = int(input('Введите число: '))
array = list(range(1, number+1))
print(array)
count = 0
start_element = 1
while count < len(array):
    start_element *= array[(start_index+1)]
    count += 1
    print(array)
print(array)


# number = int(input('Введите число: '))
# count = 0
# array = []
# startNum = 1
# nextNum=2
# while count < number:
#     array.append(startNum) 
#     startNum = startNum*nextNum
#     count += 1
#     nextNum += 1
# print (array)