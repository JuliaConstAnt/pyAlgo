# . Проанализировать скорость и сложность одного любого алгоритма из разработанных
# в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать,
# b. написать 3 варианта кода (один у вас уже есть),
# c. проанализировать 3 варианта и выбрать оптимальный,
# d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать,
# для каких N вы проводили замеры),
# e. написать общий вывод: какой из трёх вариантов лучше и почему.


# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.


def max_negative(arr_num):
    # arr_num = [-42, -28, 13, -69, 70, -37, 46, -59, 41, 38, -70, 1, -11, -25, 80, -7, -19, -19, -20, 50]
    # arr_num = [-70, -69, -59, -42, -37, -28, -25, -20, -19, -19, -11, -7, 1, 13, 38, 41, 46, 50, 70, 80]
    res = float('-inf')
    for el in arr_num:
        if res < el < 0:
            res = el
    return res


def max_negative2(arr_num):
    # arr_num = [-42, -28, 13, -69, 70, -37, 46, -59, 41, 38, -70, 1, -11, -25, 80, -7, -19, -19, -20, 50]
    # arr_num = [-70, -69, -59, -42, -37, -28, -25, -20, -19, -19, -11, -7, 1, 13, 38, 41, 46, 50, 70, 80]
    res = []
    for el in arr_num:
        if el < 0:
            res.append(el)
    return max(res)


def max_negative3(arr_num):
   # arr_num = [-42, -28, 13, -69, 70, -37, 46, -59, 41, 38, -70, 1, -11, -25, 80, -7, -19, -19, -20, 50]
   # arr_num = [-70, -69, -59, -42, -37, -28, -25, -20, -19, -19, -11, -7, 1, 13, 38, 41, 46, 50, 70, 80]
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

# timeit
# PS C:\Users\user\PycharmProjects\PyAlgo> python -m timeit -n 100000 -s "import lesson4_task1" "lesson4_task1.max_negative()"
# 100000 loops, best of 5: 1.4 usec per loop
# PS C:\Users\user\PycharmProjects\PyAlgo> python -m timeit -n 100000 -s "import lesson4_task1" "lesson4_task1.max_negative2()"
# 100000 loops, best of 5: 1.6 usec per loop
# PS C:\Users\user\PycharmProjects\PyAlgo> python -m timeit -n 100000 -s "import lesson4_task1" "lesson4_task1.max_negative3()"
# 100000 loops, best of 5: 1.52 usec per loop

# Первый алгоритм самый оптимальный, так как мы проходимся по массиву только один раз
# Во втором, даже несмотря на то, что размер массива сокращается путем отсеивания неотрицательных значений, метод max()
# использует алгоритм сортировки, что увеличивает время выполнения
# Третий алгоритм сокращает время выполнения засчет бинарного поиска, но тем не менее он требует предварительной
# сортировки массива.
# На сортированных массивах наилучший результат показывает третий алгоритм
# PS C:\Users\user\PycharmProjects\PyAlgo> python -m timeit -n 100000 -s "import lesson4_task1" "lesson4_task1.max_negative()"
# 100000 loops, best of 5: 1.42 usec per loop
# PS C:\Users\user\PycharmProjects\PyAlgo> python -m timeit -n 100000 -s "import lesson4_task1" "lesson4_task1.max_negative2()"
# 100000 loops, best of 5: 1.68 usec per loop
# PS C:\Users\user\PycharmProjects\PyAlgo> python -m timeit -n 100000 -s "import lesson4_task1" "lesson4_task1.max_negative3()"
# 100000 loops, best of 5: 1.27 usec per loop

import cProfile
import random
a1 = [random.randint(-1000000, 1000000) for i in range(random.randint(1900000, 2000000))]
a2 = [random.randint(-1000000, 1000000) for i in range(random.randint(1900000, 2000000))]
a2.sort()

cProfile.run('max_negative(a1)')
#    4 function calls in 0.080 seconds
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.080    0.080 <string>:1(<module>)
#         1    0.080    0.080    0.080    0.080 lesson4_task1.py:17(max_negative)
#         1    0.000    0.000    0.080    0.080 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('max_negative2(a1)')
#    978612 function calls in 0.352 seconds
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.007    0.007    0.352    0.352 <string>:1(<module>)
#         1    0.208    0.208    0.345    0.345 lesson4_task1.py:27(max_negative2)
#         1    0.000    0.000    0.352    0.352 {built-in method builtins.exec}
#         1    0.018    0.018    0.018    0.018 {built-in method builtins.max}
#    978607    0.119    0.000    0.119    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('max_negative3(a1)')
#    6 function calls in 0.664 seconds
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.663    0.663 <string>:1(<module>)
#         1    0.000    0.000    0.663    0.663 lesson4_task1.py:37(max_negative3)
#         1    0.000    0.000    0.664    0.664 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.663    0.663    0.663    0.663 {method 'sort' of 'list' objects}
cProfile.run('max_negative(a2)')
# 4 function calls in 0.276 seconds
cProfile.run('max_negative2(a2)')
# 976514 function calls in 0.567 seconds
cProfile.run('max_negative3(a2)')
# 6 function calls in 0.089 seconds
