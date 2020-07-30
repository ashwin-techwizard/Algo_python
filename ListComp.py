xlist= [range (0,5)]
print(type(xlist))
print(xlist)

print([x*2 for x in range (0,5)])


flip=lambda x: x[::-1]

print(flip("BVAC"))