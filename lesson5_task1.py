# 1. Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import OrderedDict

n = int(input(f'Input number of companies: '))
d = OrderedDict()
tot_income = 0
for i in range(n):
    name = input(f'Input company name: ')
    income = int(input(f'Input income: '))
    d[name] = income
    tot_income += income
mean_income = tot_income/n
print(f'Mean income is: {mean_income}')
low_lst = []
high_lst = []
for key, val in d.items():
    if val < mean_income:
        low_lst.append(key)
    elif val > mean_income:
        high_lst.append(key)
print(f'Companies with income lower than mean are: ')
for el in low_lst:
    print(el, sep=',')
print(f'Companies with income higher than mean are: ')
for el in high_lst:
    print(el, sep=',')
