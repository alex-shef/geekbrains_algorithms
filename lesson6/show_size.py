from sys import getsizeof


def show_size(x, level=0):
    result_size = getsizeof(x)
    print('\t' * level, f'type={x.__class__}, size={getsizeof(x)}, object={x}')

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                result_size += show_size(xx, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                result_size += show_size(xx, level + 1)
    return result_size
