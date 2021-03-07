# Если начальные значения диапазонов равны (min_range = min_num)

from lesson6.show_size import show_size


def multiple(max_range=99, min_num=2, max_num=9):
    count = {}
    for i in range(min_num, max_num + 1):
        count[i] = max_range // i

    print('Общий размер переменных', show_size(locals()))
    return count


multiple()


'''
Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32

type=<class 'dict'>, size=232, object={'max_range': 99, 'min_num': 2, 'max_num': 9, 'count': {2: 49, 3: 33, 4: 24, 5: 19, 6: 16, 7: 14, 8: 12, 9: 11}, 'i': 9}
	 type=<class 'tuple'>, size=56, object=('max_range', 99)
		 type=<class 'str'>, size=58, object=max_range
		 type=<class 'int'>, size=28, object=99
	 type=<class 'tuple'>, size=56, object=('min_num', 2)
		 type=<class 'str'>, size=56, object=min_num
		 type=<class 'int'>, size=28, object=2
	 type=<class 'tuple'>, size=56, object=('max_num', 9)
		 type=<class 'str'>, size=56, object=max_num
		 type=<class 'int'>, size=28, object=9
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
	 type=<class 'tuple'>, size=56, object=('i', 9)
		 type=<class 'str'>, size=50, object=i
		 type=<class 'int'>, size=28, object=9
		 
Общий размер переменных 2154
'''