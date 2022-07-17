#n = int(input("--> "))
#a = 1
#for i in range(1,n+1):
 #   a = a*i
#print(a)

# доработка
N = int(input("Введите N для набора произведений чисел от 1 до N: "))
lst = [1]
for i in range(2, N+1):
    lst.append(lst[i-2] * i)
print (f"Итоговый набор {lst}")