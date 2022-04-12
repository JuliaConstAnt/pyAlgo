# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями
# 0, 3, 4, 5 (помните, что индексация начинается с нуля),
# т. к. именно в этих позициях первого массива стоят четные числа.

def save_indexes_in_arr(array):
    a2 = []
    for el in array:
        if el % 2 == 0:
            a2.append(array.index(el))
    return a2

import random
a1 = [random.randint(-100, 100) for i in range(random.randint(10, 20))]
a2 = save_indexes_in_arr(a1)
print(a1)
print(a2)
