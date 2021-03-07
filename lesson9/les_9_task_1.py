"""
Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.
"""

from hashlib import sha1


def count(s):
    length = len(s)
    hash_set = set()
    for i in range(length):
        for j in range(i, length+1):
            if s[i:j] and s[i:j] != s:
                hash_set.add(sha1(s[i:j].encode('utf-8')).hexdigest())
                # print(s[i:j])

    return len(hash_set)


string = input('Введите строку: ')

print(f'Кол-во подстрок в строке "{string}" равно {count(string)}')
