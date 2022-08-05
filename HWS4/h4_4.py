# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


from random import randint

path = 'D:\python/HWS4/55.txt'

k=2
with open(path, 'w') as file:
    file.write(f'{randint(0,100)} * x**{k} + {randint(0,100)} * x**{k-1}  + {randint(0,100)} = 0\n')
    file.write(f'x**{k} + {randint(0,100)} = 0\n')
    file.write(f'{randint(0,100)} * x**{k-1}  + {randint(0,100)} = 0')