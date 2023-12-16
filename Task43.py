"""
Задача №43. Решение в группах
Дан список чисел. Посчитайте, сколько в нем пар
элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных
строках.
Ввод:
1 2 3 2 3
Вывод:
2
"""
from random import randint

# list_1 = [randint(1, 10) for _ in range(10)]
list_1 = [1, 2, 3, 2, 3, 3, 3]
print(list_1)
pair_count = list(list_1.count(el) // 2 for el in set(list_1))
print(len(set(pair_count)))
