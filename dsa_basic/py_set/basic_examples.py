"""
Operators	Notes
key in s	containment check
key not in s	non-containment check
s1 == s2	s1 is equivalent to s2
s1 != s2	s1 is not equivalent to s2
s1 <= s2	s1 is subset of s2
s1 < s2	s1 is proper subset of s2
s1 >= s2	s1 is superset of s2
s1 > s2	s1 is proper superset of s2
s1 | s2	the union of s1 and s2
s1 & s2	the intersection of s1 and s2
s1 - s2	the set of elements in s1 but not s2
s1 ˆ s2	the set of elements in precisely one of s1 or s2

ref: gfg

"""


def display_sets_ele(set_init: set) -> None:
    # ele wise display
    for _ele in set_init:
        print(_ele, end=' ')
    # all set ele at once
    print(f'\n{set_init = }')
    pass


def set_addition(set_init_add: set) -> None:
    # non-existing element add and return
    set_init_add.add(100)
    # existing ele addition
    set_init_add.add(5)
    # call display method to get new view  of the set after addition
    print('calling display method after add methods')
    display_sets_ele(set_init_add)

    pass


def set_removal(set_init_remove: set, key=1000) -> None:
    # lets make the copy of the ori set using shallow  coping
    ori_set_init_remove = set_init_remove.copy()

    # existing key removal
    set_init_remove.remove(0)
    # non-existing key removal  1000
    try:
        set_init_remove.remove(key)
    except KeyError as ke:
        print(f'key error occured for: {key=}, no existing key in the set')

    print(f'{ori_set_init_remove=}')
    print(f'{set_init_remove=}')

    pass


def set_discard(set_init, key):
    # let's keep the copy or ori
    ori_set = set_init.copy()
    # let's now use the discard methods
    set_init.discard(key)
    print(f'{ori_set = }')
    print(f'{set_init = }')


def adding_immutable_seq(set_init: set) -> None:
    # mutable/unhashable seq.
    lst = [1, 2, 3]
    # mutable/unhashable seq.
    dct = {'hashable': 'No'}
    # immutable/hashable seq.
    tpl = (1, 3, 4)
    #
    set_init.add(tpl)
    try:
        set_init.add(lst)
    except TypeError as e:
        print(f'Exception occurred: {str(e)}')
    try:
        set_init.add(dct)
    except TypeError as e:
        print(f'Exception occurred: {str(e)}')


if __name__ == '__main__':
    set_init = set()
    # let's try adding immutable seq to the set
    adding_immutable_seq(set_init)

    # add ele to the set
    for ele in range(10):
        set_init.add(ele)  # adding with add
    print('init set display')
    display_sets_ele(set_init)

    # built-in add ele
    set_addition(set_init)

    # built-in remove
    set_removal(set_init, key=1000)

    # built-in discard( handles gracefully for missing key)
    set_discard(set_init, key=100)

    # set OPERATION (union, intersection, set difference , sub-set, super-set)
    set_a = {ele for ele in range(10)}
    set_b = {ele for ele in range(5, 15)}

    # set union
    union_set = set_a.union(set_b)
    # or
    union_set_oprator = set_a | set_b
    print(f'{union_set_oprator = }')
    print(f'{union_set = }')

    # set intersection
    intersection_set = set_a.intersection(set_b)
    # or
    intersection_set_opreator = set_a & set_b
    print(f'{intersection_set_opreator = }')
    print(f'{intersection_set = }')

    #  set difference
    set_difference = set_b.difference(set_a)
    # or
    set_difference_operator = set_b - set_a
    print(f'{set_difference = }')
    print(f'{ set_difference_operator = }')
