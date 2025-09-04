






def rev_only_num(input: str):
    i, j = 0, len(input)-1
    input_list = list(input)
    while i < j:
        if str(input_list[i]).isdigit() and str(input[j]).isdigit():
            input_list[i], input_list[j] = input_list[j], input_list[i]
            i += 1
            j -= 1
        elif not str(input_list[i]).isdigit():
            i += 1
        else:
            j -= 1
    return ''.join(input_list)


print(rev_only_num("$1,234"))
