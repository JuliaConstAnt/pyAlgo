# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

def max_negative (arr_num):
    res = float('-inf')
    i_res = 0
    for el in arr_num:
        if res < el < 0:
            i_res = arr_num.index(el)
            res = el
    return res, i_res

import random
a = [random.randint(-100, 100) for i in range(random.randint(10, 20))]
num, ind = max_negative(a)
print(f'В массиве {a} \nмаксимальный отрицательный элемент: {num} с индексом {ind}')