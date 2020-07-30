# 1)	Write a program which will find numbers which are divisible by 7 but not a multiple of 5 between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.
print(','.join(map(str, filter(lambda x:  (x % 5 != 0) and (x % 7 == 0), range(2000, 3200)))))


print(",".join(map(str,[ x for x in range(2000, 3200) if (x % 5 != 0) and (x % 7 == 0) ])))


# 2)	Write a program to find largest sequence in a given list of numbers
# INPUT = [1,2,3,2,4,5,6,7,8,1,0,4,5,6]
# Expected Result: [4, 5, 6, 7, 8]


from itertools import groupby
input= [1,2,3,2,4,5,6,7,8,1,0,4,5,6]
grouped = []
for k,g in groupby(enumerate(input), lambda en: (print('dif',(en[0] - en[1])), en[0] - en[1])):
    grouped.append(list(map(lambda tup: tup[1], g)))
print(max(grouped, key=lambda x: len(x)))



# 3)	Write a program to print the possible combinations of any given word
# INPUT = "CAT"
# Expected Result:  "CAT","CTA","ACT","ATC","TCA","TAC"




def Combinations(inpStr, prev=''):
    if len(inpStr) == 0:
        print(prev)
    else:
        for i in range(len(inpStr)):
            sub = inpStr[0:i] + inpStr[i + 1:]
            Combinations(sub, prev + inpStr[i])

Combinations('cat')



def spin_words(sentence):
        
    return " ".join([word[::-1] if (len(word) >= 5) else word for word in sentence.split()])


def likes(names):
    out = {
            0: "no one likes this",
            1: "{} likes this",
            2: "{} and {} like this",
            3: "{}, {} and {} like this",
            4: "{}, {} and {others} others like this"
        }
    n = len(names)
    v=10
    print(min(v,4))
    print(type(names))
    print("{}, {} ,{} and {others} others like this".format(*names,others=n-3))
    return out[min(n,4)].format(*names, others=n-2)


print(likes(["Alex", "Jacob", "Mark", "Max"] ))



