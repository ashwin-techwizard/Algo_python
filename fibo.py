import sys

num=int(sys.argv[1])

current=0

def fibo(prev ,curr,index):
    print(prev)
    sum=prev+curr
    index=index+1
    if(index<num):
        fibo(curr,sum,index)


fibo(current,1,0)

n1,n2=0,1
while(current<num):
    # print(current)
    print(n1)
    sum=n1+n2
    n1=n2
    n2=sum
    current=current+1

