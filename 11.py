def sequence_sum(begin_number, end_number, step):
    return sum(range(begin_number, end_number+1, step))




print(sequence_sum(2, 6, 2))  # 12)
print(sequence_sum(1, 5, 1))  # 15)
print(sequence_sum(1, 5, 3))  # 5)
print(sequence_sum(0, 15, 3))  # 45)

#2,2,2 --> 2
#2,6,2 --> 12 (2 + 4 + 6)
#1,5,1 --> 15 (1 + 2 + 3 + 4 + 5)
#1,5,3  --> 5 (1 + 4)


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
