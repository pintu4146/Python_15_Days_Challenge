"""
let's compare the list comp and generator expression in terms of memory it can take

"""
import sys


def generator_function() -> None:
    for ele in range(1000):
        yield ele


def memory_use_list_comp() -> None:
    list_comp = [ele for ele in range(100000)]
    gen_exprs = (ele for ele in range(100000))
    print(f'list comprehension : {list_comp}')
    print(f'gen expression', {gen_exprs})
    print(f' memory used using list comprehension: {sys.getsizeof(list_comp)}')
    print(f' memory used using generator comprehension: {sys.getsizeof(gen_exprs)}')


if __name__ == '__main__':
    memory_use_list_comp()
    print(f'gen funct : {sys.getsizeof(generator_function())}')
