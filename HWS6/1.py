# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример:

# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

# list1 = [1, 2, 3, 5, 1, 5, 3, 10]
list1 = [int(i) for i in input().split()]  #заполняем список 
# [listUnic.append(i) for i in list1 if  list1.count(i)==1] #можно и так
listUnic = list(filter(lambda x:list1.count(x)==1, list1)) # записываем уникальные элементы через filter
print(f'{list1} -> {listUnic}')

# Найти сумму чисел списка стоящих на нечетной позиции


list1 = [int(i) for i in input().split()]  # заполняем список

# res = sum(list[::2]) # так проще всего

# с использованием лямбд, filter, map, enumerate
en = enumerate(list1)
# print(en)
res = list(filter(lambda x:x[0]%2 == 0, en)) #предполагаем что позиция 1 - нечетная, соответствует индексу 0 (четному)
res = list(map(lambda x:x[1], res ))
result = sum(res)

print (f'{list1} -> {result}')

    