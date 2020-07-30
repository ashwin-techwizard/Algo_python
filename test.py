from itertools import groupby

tst1="2 4 7 8 10"
tst="9 1 7 4 5"
lil="10 31 0 36 10 26 26"
tstin=[int(x) for x in tst1.split()]

iseven= lambda x : x%2==0

isodd = lambda x: x % 2 != 0
 
#print ([ groupby(ex,key=iseven) for ex in tstin])            

print(type(groupby(tstin,iseven)))

# ff={groupby(tstin,iseven)}
# print(list(ff))
key_and_group={}
for k,g in groupby(tstin,iseven):
    print(k)
    group=list(g)
    print(group)
    if(k in key_and_group):
 
        another_list = key_and_group.pop(k)
 
        print (type(another_list)) 
        print (type(group))
        group.extend(another_list)
        print(group)
        key_and_group[k]=group
    else:
        key_and_group[k]=group
    # if(len(group)==1):
print(key_and_group)
print(">>>",min(key_and_group,key=lambda k: len(key_and_group[k])))
print(tstin.index(key_and_group[min(key_and_group,key=lambda k: len(key_and_group[k]))][0])+1)