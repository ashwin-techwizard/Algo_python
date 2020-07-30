inlist=[-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]


from itertools import groupby
input= [1,2,3,2,4,5,6,7,8,1,0,4,5,6]
grouped = []
for k,g in groupby(enumerate(inlist), lambda en: (print('dif',(en[0] - en[1])), en[0] - en[1])):
    grouped.append(list(map(lambda tup: tup[1], g)))
print(grouped)

print([xlist for xlist in grouped])

def mapFun(in_list):
    length=len(in_list)
    print(">>",length)
    if(length<2):
        return str(in_list[0])
    else:
        return str(in_list[0])+"-"+str(in_list[length-1])
#print([x for x in map(mapFun,grouped)])
print(",".join(map(mapFun,grouped)))

print(max(grouped, key=lambda x: len(x)))


# Other
def solution(args):
    out = []
    beg = end = args[0]
    
    for n in args[1:] + [""]:        
        if n != end + 1:
            if end == beg:
                out.append( str(beg) )
            elif end == beg + 1:
                out.extend( [str(beg), str(end)] )
            else:
                out.append( str(beg) + "-" + str(end) )
            beg = n
        end = n
    
    return ",".join(out)