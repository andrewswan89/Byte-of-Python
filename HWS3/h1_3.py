#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

#Пример:- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

#- C -> на нечётных позициях элементы 3 и 9, ответ: 12

list = [2, 3, 5, 9, 3]
sum = 0

for i in range (1, len(list), 2):
 sum +=list[i]

print(sum)