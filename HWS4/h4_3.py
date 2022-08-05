# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


def find_uniq(my_list: list) -> list:
    new_list = []
    for i in my_list:
        if i in new_list:
            continue
        else:
            new_list.append(i)
    return new_list


my_list = [12, 4, 'al', 8, 69, 'al', 7, 5, 'le']
print('Изначальный список:', my_list)
print('Итоговый список', find_uniq(my_list))