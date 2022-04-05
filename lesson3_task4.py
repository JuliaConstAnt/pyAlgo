# 4. Определить, какое число в массиве встречается чаще всего.

def most_common_num(array):
    d = {}
    for el in array:
        if el not in d:
            d.update({el: 1})
        else:
            d[el] +=1
    max = 0
    num = 0
    for key, val in d.items():
        if val >= max:
            max = val
            num = key
    return num

import random
a = [random.randint(0, 10) for i in range(random.randint(10, 30))]
print(f'В массиве {a} \nчаще всего встречается число {most_common_num(a)}')
