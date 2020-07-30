


print("GGHH"*5)

def pyfunc(r):
    for x in range(r):
        print(' '*(r-x-1)+'*'*(2*x+1))    
pyfunc(20)

list1 = ['s', 'r', 'a', 's'] 
list2 = ['a', 'a', 'n', 'h']

print(list1.pop(1))
hh= [",".join([i, j]) for i, j in zip(list1, list2)]

hh= ",".join(map(str,list2))
print(hh)

print([(i,j) for i, j in zip(list1,list2)])


# from itertools import groupby
# input= [1,2,3,2,4,5,6,7,8,1,0,4,5,6]
# grouped = []
# for k,g in groupby(enumerate(inlist), lambda en: (print('dif',en), en[0] - en[1])):
#     print("key>>"+str(k)+"   >>"+str(g))
#     grouped.append(list(map(lambda tup: tup[1], g)))
# print(grouped)

ord('A')

ord('a')
# 97
bin(123)
# '0b1111011'

alphaDict={}
print(type(alphaDict))
x=1
for i in range(97,123):

    alphaDict[chr(i)]=x
    x=x+1
    print(chr(i),end=",")


print(alphaDict)