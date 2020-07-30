x=['a','a','b','b','a','c']
prev=''
outList=[]
for ele in x:
    if(ele != prev):       
        print(ele)
        outList.append(ele)
    prev=ele

print(type(x))
print(outList)
 
n=4
import math
def is_square(n):
    if(n<0):
        return False
    # elif(int(math.sqrt(n))==n):
    #     return True
    else:
        sr = math.sqrt(n) 
        print(">>",sr)
        return ((sr - math.floor(sr)) == 0) 


print(is_square(25))


def spin_words(sentence):
    outList=[]
    for word in sentence.split():
        outList.append(word[::-1])
        
    return " ".join([word[::-1] if (len(word) % 2) != 0 else word for word in sentence.split()])

print(spin_words("Welcome"))

gg="Welcome"

print((len(gg) % 2))