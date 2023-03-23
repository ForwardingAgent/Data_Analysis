

def invert(foo):
    def wraper(*args, **kwargs):
        pass
    pass


def foo(lenght: int = 8):
    lst = [x for x in range(lenght)]
    lst1 = list(filter(lambda x: x % 2 == 0, lst))
    return lst1


def test():
    assert foo(8) == [0, 2, 4, 6]
    assert foo(4) == [0, 2]
    assert foo(-4) == [-2]


test()

def jurnal(student, math, **marks):
    print(f'Student Name: {student}')
    print(marks)
    for mark in marks:
        print(mark)


jurnal('Mike', 10, 30, 45)