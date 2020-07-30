def iq_test1(numbers):
    e = [int(i) % 2 == 0 for i in numbers.split()]

    return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1

from itertools import groupby

def iq_test(numbers):
    tstin=[int(x) for x in numbers.split()]

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
            # print("TTO>",type(key_and_group.get(k)))
            # print("BB>",key_and_group.get(k).append(group))
            # my_list = ['geeks', 'for'] 
            another_list = key_and_group.pop(k)
            #my_list.extend(group) 
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
    return tstin.index(key_and_group[min(key_and_group,key=lambda k: len(key_and_group[k]))][0])+1