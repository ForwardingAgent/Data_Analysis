class Graph:
    LIMIT_Y = [0, 10]

    def set_data(self, data):
        self.data = data
        self.lst = filter(lambda x: (self.LIMIT_Y[0] <= x <= self.LIMIT_Y[1]), self.data)

    def draw(self):
        print(*self.lst)


graph_1 = Graph()
graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw()


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
