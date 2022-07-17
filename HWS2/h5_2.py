
import random

def mix_list(list_original):
    list = list_original[:]
    list_length = len(list)
    for i in range(list_length):
        index_ran = random.randint(0, list_length - 1)
        temp = list[i]
        list[i] = list[index_ran]
        list[index_ran] = temp
    return list

list = [1, 3, 4, 6, 7, 9]
mixed_list = mix_list(list)
print("Исходный список: ")
print(list)
print("Перемешанный список: ")
print(mixed_list)