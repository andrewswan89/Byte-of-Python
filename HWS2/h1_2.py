# неверное решетие работает только с целыми
# num = int(input("Число--> "))
#sum = 0
#while (num != 0):
 #   sum = sum + num % 10
#  num = num // 10
# print("Сумма =  ", sum)

# 
num = input('Введите число: ')
sum = 0
for i in num:
    if i == '.':
        continue
    sum += int(i)
print(sum)

  #решение со списком и функцией split

#number = float(input("Введите вещественное число: "))
#lst = list(str(number).split('.'))
#summ = 0
#for i in lst:
 #   for j in i:
  #      summ += int(j)
#print(f"Сумма цифр вещественного числа равна = {summ}")
