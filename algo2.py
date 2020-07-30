

st="Success".lower()#"recede"

print("".join(map(str,[')' if (st.count(v) > 1 ) else '(' for v in st ])))

x=[20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]

print([x.count(v) for v in x])

print([v for v in x if (x.count(v) % 2)!=0][0])


from itertools import groupby

def find_it1(seq):
    return next(k for k, g in groupby(sorted(seq)) if len(list(g)) % 2)

from operator import xor
import functools 
def find_it2(seq):
    return functools.reduce(xor, seq)

print(find_it1(x))
print(find_it2(x))

def find_less(seq):
    return functools.reduce(lambda a,b: b if (b < a) else a , seq)

print(find_less(x))


