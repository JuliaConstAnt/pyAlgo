# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления,
# задача решается в несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит.
# Поэтому использование встроенных функций для перевода из одной системы счисления в другую
# в данной задаче под запретом.

from collections import deque


def hex_to_int(s):
    hx = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
          'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    h = s.copy()
    res = 0
    i = 0
    while len(h):
        res += hx[h.pop()] * 16**i
        i += 1
    return res


def int_to_hex(num):
    i = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
         10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    res = deque()
    tmp = num
    while tmp // 16 > 0:
        res.appendleft(i[tmp % 16].upper())
        tmp = tmp // 16
    res.appendleft(i[tmp % 16].upper())
    s = ''
    for el in res:
        s += el
    return s


s1 = deque(input('Input 1st number: ').upper())
s2 = deque(input('Input 2nd number: ').upper())

print(int_to_hex(hex_to_int(s1) + hex_to_int(s2)))
print(int_to_hex(hex_to_int(s1) * hex_to_int(s2)))
