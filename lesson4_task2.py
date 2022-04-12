# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
# Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.
from math import sqrt
import cProfile


def eratosphen(n):
    count = 1
    i = 2
    num = 1000
    res = 2
    while count < n:
        a = True
        for x in range(i, num + 2):
            if x % 2:
                for y in range(3, num + 2):
                    if y % 2:
                        if x != y and y != 1:
                            if not x % y:
                                a = False
                                break
                if a == True:
                    count += 1
                    res = x
                if count == n:
                    return res, count
                a = True
        i += 1000
        num += 1000


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i += 2
    return True


def primes(n):
    i = 1
    num = 1000
    count = 0
    res = 0
    while count < n:
        for el in range(i, num + 1):
            if is_prime(el):
                count += 1
                res = el
            if count == n:
                return res, count
        i += 1000
        num += 1000


cProfile.run('eratosphen(1000)')
# 4 function calls in 0.229 seconds
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.229    0.229 <string>:1(<module>)
#         1    0.229    0.229    0.229    0.229 lesson4_task2.py:13(eratosphen)
#         1    0.000    0.000    0.229    0.229 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('primes(1000)')
# 49501 function calls in 0.014 seconds
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.014    0.014 <string>:1(<module>)
#      7919    0.008    0.000    0.013    0.000 lesson4_task2.py:38(is_prime)
#         1    0.001    0.001    0.014    0.014 lesson4_task2.py:53(primes)
#         1    0.000    0.000    0.014    0.014 {built-in method builtins.exec}
#     41578    0.005    0.000    0.005    0.000 {built-in method math.sqrt}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Второй алгоритм работает значительно быстрее, несмотря на большее количество вызовов