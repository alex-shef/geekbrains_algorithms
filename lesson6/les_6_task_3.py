from lesson6.show_size import show_size


def multiple(min_range=2, max_range=99):
    count = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

    for num in range(min_range, max_range + 1):

        if num % 2 == 0:
            count[2] += 1

        if num % 3 == 0:
            count[3] += 1

        if num % 4 == 0:
            count[4] += 1

        if num % 5 == 0:
            count[5] += 1

        if num % 6 == 0:
            count[6] += 1

        if num % 7 == 0:
            count[7] += 1

        if num % 8 == 0:
            count[8] += 1

        if num % 9 == 0:
            count[9] += 1

    print('Общий размер переменных', show_size(locals()))
    return count


multiple()


'''
Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32

 type=<class 'dict'>, size=232, object={'min_range': 2, 'max_range': 99, 'count': {2: 49, 3: 33, 4: 24, 5: 19, 6: 16, 7: 14, 8: 12, 9: 11}, 'num': 99}
	 type=<class 'tuple'>, size=56, object=('min_range', 2)
		 type=<class 'str'>, size=58, object=min_range
		 type=<class 'int'>, size=28, object=2
	 type=<class 'tuple'>, size=56, object=('max_range', 99)
		 type=<class 'str'>, size=58, object=max_range
		 type=<class 'int'>, size=28, object=99
	 type=<class 'tuple'>, size=56, object=('count', {2: 49, 3: 33, 4: 24, 5: 19, 6: 16, 7: 14, 8: 12, 9: 11})
		 type=<class 'str'>, size=54, object=count
		 type=<class 'dict'>, size=360, object={2: 49, 3: 33, 4: 24, 5: 19, 6: 16, 7: 14, 8: 12, 9: 11}
			 type=<class 'tuple'>, size=56, object=(2, 49)
				 type=<class 'int'>, size=28, object=2
				 type=<class 'int'>, size=28, object=49
			 type=<class 'tuple'>, size=56, object=(3, 33)
				 type=<class 'int'>, size=28, object=3
				 type=<class 'int'>, size=28, object=33
			 type=<class 'tuple'>, size=56, object=(4, 24)
				 type=<class 'int'>, size=28, object=4
				 type=<class 'int'>, size=28, object=24
			 type=<class 'tuple'>, size=56, object=(5, 19)
				 type=<class 'int'>, size=28, object=5
				 type=<class 'int'>, size=28, object=19
			 type=<class 'tuple'>, size=56, object=(6, 16)
				 type=<class 'int'>, size=28, object=6
				 type=<class 'int'>, size=28, object=16
			 type=<class 'tuple'>, size=56, object=(7, 14)
				 type=<class 'int'>, size=28, object=7
				 type=<class 'int'>, size=28, object=14
			 type=<class 'tuple'>, size=56, object=(8, 12)
				 type=<class 'int'>, size=28, object=8
				 type=<class 'int'>, size=28, object=12
			 type=<class 'tuple'>, size=56, object=(9, 11)
				 type=<class 'int'>, size=28, object=9
				 type=<class 'int'>, size=28, object=11
	 type=<class 'tuple'>, size=56, object=('num', 99)
		 type=<class 'str'>, size=52, object=num
		 type=<class 'int'>, size=28, object=99
		 
Общий размер переменных 2018 - наименьший из трёх.
Но необходимо изменять код при изменении диапазона от 2 до 9.
Не подходит при большом дипазоне.
'''
