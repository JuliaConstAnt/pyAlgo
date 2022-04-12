# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

def change_min_max(array):
    i_min = 0
    i_max = 0
    min = 0
    max = 0
    for el in array:
        if el <= min:
            i_min = array.index(el)
            min = el
        if el >= max:
            i_max = array.index(el)
            max = el
    array[i_min] = max
    array[i_max] = min


import random
a = [random.randint(-100, 100) for i in range(random.randint(10, 20))]
print(a)
change_min_max(a)
print(a)