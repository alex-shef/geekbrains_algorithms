# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.

min_range = 2
max_range = 99
min_num = 2
max_num = 9

for i in range(min_num, max_num + 1):
    count = 0
    for j in range(min_range, max_range + 1):
        if j % i == 0:
            count += 1
    print(f'Числу {i} кратно {count} чисел')
