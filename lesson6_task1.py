#  Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых
#  трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
# b. написать 3 варианта кода (один у вас уже есть);
# проанализировать 3 варианта и выбрать оптимальный;
#
# c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев
# в файл с кодом. Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
# d. написать общий вывод: какой из трёх вариантов лучше и почему.

# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.
from memory_profiler import profile
import random


@profile
def max_negative(arr_num):
    res = float('-inf')
    for el in arr_num:
        if res < el < 0:
            res = el
    return res


@profile
def max_negative2(arr_num):
    res = []
    for el in arr_num:
        if el < 0:
            res.append(el)
    return max(res)


@profile
def max_negative3(arr_num):
    arr_num.sort()
    beg = 0
    end = len(arr_num)-1
    if arr_num[end] < 0:
        return arr_num[end]
    while beg < end and beg+1 != end:
        if arr_num[(beg + end)//2] >= 0:
            end = (beg + end)//2
        else:
            beg = (beg + end)//2
    return arr_num[beg]


a1 = [random.randint(-1000000, 1000000) for i in range(random.randint(1900000, 2000000))]
max_negative(a1)
# Python 3.8.10, Win64
# memory profiler
# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     19     92.2 MiB     92.2 MiB           1   @profile
#     20                                         def max_negative(arr_num):
#     21     92.2 MiB      0.0 MiB           1       res = float('-inf')
#     22     92.3 MiB -20432.5 MiB     1909988       for el in arr_num:
#     23     92.3 MiB -20432.5 MiB     1909987           if res < el < 0:
#     24     92.3 MiB      0.0 MiB          16               res = el
#     25     92.2 MiB     -0.1 MiB           1       return res

max_negative2(a1)
# memory profiler
# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     28     92.2 MiB     92.2 MiB           1   @profile
#     29                                         def max_negative2(arr_num):
#     30     92.2 MiB      0.0 MiB           1       res = []
#     31     99.5 MiB -456883.6 MiB     1909988       for el in arr_num:
#     32     99.5 MiB -456883.6 MiB     1909987           if el < 0:
#     33     99.5 MiB -227603.7 MiB      954005               res.append(el)
#     34     99.5 MiB      0.0 MiB           1       return max(res)

max_negative3(a1)
# memory profiler
# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     37     92.2 MiB     92.2 MiB           1   @profile
#     38                                         def max_negative3(arr_num):
#     39     93.8 MiB      1.6 MiB           1       arr_num.sort()
#     40     93.8 MiB      0.0 MiB           1       beg = 0
#     41     93.8 MiB      0.0 MiB           1       end = len(arr_num)-1
#     42     93.8 MiB      0.0 MiB           1       if arr_num[end] < 0:
#     43                                                 return arr_num[end]
#     44     93.8 MiB      0.0 MiB          22       while beg < end and beg+1 != end:
#     45     93.8 MiB      0.0 MiB          21           if arr_num[(beg + end)//2] >= 0:
#     46     93.8 MiB      0.0 MiB           7               end = (beg + end)//2
#     47                                                 else:
#     48     93.8 MiB      0.0 MiB          14               beg = (beg + end)//2
#     49     93.8 MiB      0.0 MiB           1       return arr_num[beg]

