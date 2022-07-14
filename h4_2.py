arr = [int(input('Введите элемент списка--> ')) for i in range(int(input('Введите длину --> ')))]
 
prod = 1
for i in arr:
    prod *= i
 
print(f'Список--> {arr}')
print(f'Произведение--> {prod}')