import random

class Line:

    def __init__(self, a, b, c, d):
        self.a = a, 
        self.b = b,
        self.c = c, 
        self.d = d
        sp = (self.a, self.b)
        ep = (self.c, self.d)
        
    
class Rect:
    def __init__(self, a, b, c, d):
        self.a = a, 
        self.b = b,
        self.c = c, 
        self.d = d
        sp = (self.a, self.b)
        ep = (self.c, self.d)

class Ellipse:
    def __init__(self, a, b, c, d):
        self.a = a, 
        self.b = b,
        self.c = c, 
        self.d = d
        sp = (self.a, self.b)
        ep = (self.c, self.d)


a = 1
b = 2
c = 3
d = 4
g1 = Line(a, b, c, d)
g2 = Rect(a, b, c, d)
g3 = Ellipse(a, b, c, d)


# далее ее сплитим по Enter line.split('\n'), 
# получаем список типа ['tree - дерево', ..., ...], 
# для каждого item которого eng_word, rus_word = (item.split(' - ')), 
# затем вызываем метод tr.add(eng_word, rus_word)


class Notes:
    pass
# 
# 
# mydict = {
#     'uid': 1005435,
#     'title': "Шутка",
#     'author': "И.С. Бах",
#     'pages': 2
# }
# for at, val in mydict.items():
#     setattr(Notes, at, val)
# print(getattr(Notes, 'author'))

#import sys
# 
#j = sys.stdin.readline().strip()
#s = sys.stdin.readline().strip()
#print(j)
#print(s)
#result = 0
#for ch in s:
#    if ch in j:
#        result += 1
#print(result)


#n = int(input())
#s = set()
##s.add(m) for m = int(input()) 
#for i in range(n):
#    m = int(input())
#    s.add(m)
##s = sorted(s)
#[print(j) for j in sorted(s)]

#def minus(string: str, word: str) -> str:
#    if string.startswith(word):
#        return string.replace(word, '', 1)
    #if string[:(len(word))] == word:
    #    return string[len(word):]
    #else:
    #    return string

# assert minus('Привет мой друг', 'Прив') == 'ет мой друг'
# assert minus('Привет мой друг', 'мой') == 'Привет мой друг'


#class DifStr(str):
#    def __init__(self, string) -> None:
#        self.string = string
#
#    def __sub__(self, word):
#        self.word = word
#        if self.string.startswith(self.word):
#            return self.string.replace(self.word, '', 1)
#        return self.string
#
#
#d = DifStr('aaa')
#print(d - 'a')
