def make_list(length, value=0):
    lst = []
    [lst.append(value) for x in range(length)]
    return print(f'result = {lst}')


result = make_list(3)
result = make_list(5, 1)