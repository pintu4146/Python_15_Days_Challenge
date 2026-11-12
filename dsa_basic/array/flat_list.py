"""
input_list-[1,[2,3],[4,[5,6]]]
op - [1,2,3,4,5,6]

"""


def flat_list(nst_list: list) -> list:
    rtn = []
    for ele in nst_list:
        if isinstance(ele, list):
            rtn.extend(flat_list(ele))
        else:
            rtn.append(ele)
    return rtn


print(flat_list([1, [2, 3], [[4, [5, 6],7]]]))
