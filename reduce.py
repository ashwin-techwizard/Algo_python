alphaDict={}
print(type(alphaDict))
x=1
for i in range(97,123):

    alphaDict[chr(i)]=x
    x=x+1

print(alphaDict)

tst="abc"


def reducFun(a_word="",b_word=""):
    a_sum=sum([alphaDict[letter] for letter in a_word])
    b_sum=sum([alphaDict[letter] for letter in b_word])
    if(a_sum>=b_sum):
        return a_word
    else:
        return b_word

sent="what time are we climbing up the volcano bmwtyeuxn should equal xniggqcrzv"

print(max(sent.split(),key=lambda sm: sum(ord(c)-96 for c in sm)))

print(sum(ord(c)-96 for c in tst) for tst in sent.split())

import functools

print(functools.reduce(reducFun,[ x for x in sent.split() ]))

def high(x):
    s, n = x.split(), [sum(ord(c) - 96 for c in y) for y in x.split()]
    return s[n.index(max(n))]

def high(words):
    return max(words.split(), key=lambda word: sum(ord(c) - ord('a') + 1 for c in word.lower()))

def high(s):
    s = ''.join([x for x in s if x.isdigit() != True])
    result = []
    a = dict([[y, x] for x, y in enumerate(list(map(chr, range(97, 123))), 1)])
    for i in s.lower().split():
        result.append(sum([a[c] for c in i]))
    return s.split()[result.index(max(result))]