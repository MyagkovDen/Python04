# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений 
# в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18

# 6 12

from random import randint

n, m = int(input('n: ')), int(input('m: '))
lst_1 , lst_2 = [], []
for i in range(n):
    lst_1.append(randint(1, 20))
for i in range(m):
    lst_2.append(randint(1, 20))
print(lst_1)
print(lst_2)

set_1, set_2 = set(lst_1), set(lst_2)
#print(set_1)
#print(set_2)

print(*sorted(set_1.intersection(set_2)))