"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за четыре квартала для каждого предприятия. Программа должна определить
среднюю прибыль (за год для всех предприятий) и отдельно вывести
наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""

from collections import namedtuple


Enterprises = namedtuple('Enterprises', 'name quarter1 quarter2 quarter3 quarter4 year_profit')
count = int(input('Количество предприятий: '))
total_profit = 0
enterprise = []

for i in range(count):
    name = input(f'Наименование {i+1}-го предприятия: ')
    quarters = [float(j) for j in input('Прибыль в каждом из 4 кварталов, через пробел: ').split()]
    year_profit = 0
    for quarter in quarters:
        year_profit += quarter
    total_profit += year_profit

    enterprise.append(Enterprises(name, *quarters, year_profit))

if count == 1:
    print(f'Годовая прибыль {enterprise[0].name}: {enterprise[0].year_profit}.')

else:
    average_profit = total_profit / count

    less_average = []
    more_average = []

    for i in range(count):

        if enterprise[i].year_profit < average_profit:
            less_average.append(enterprise[i])

        elif enterprise[i].year_profit > average_profit:
            more_average.append(enterprise[i])

    print(f'\nСредняя годовая прибыль: {average_profit}')

    print(f'Предприятия, чья прибыль меньше {average_profit}:')
    for enterprise in less_average:
        print(f'"{enterprise.name}" с прибылью {enterprise.year_profit}')

    print(f'\nПредприятия, чья прибыль больше {average_profit}:')
    for enterprise in more_average:
        print(f'"{enterprise.name}" с прибылью {enterprise.year_profit}')
