str_list = 'Привет, Мир! Мы очабв любим Пайтонабв! Семинары'
str_list= str_list.split()
def strs(str):
    for item in str_list:
        if 'абв' in item:
            str_list.remove(item)
    print(str_list)
strs(str_list)
res = list(filter(lambda item: 'абв' not in item, str_list.split()))
print(res)