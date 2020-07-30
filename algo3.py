
def array_diff(a, b):
    print([x for x in a if not(x in b)])

array_diff([1,2],[1])


def order(sentence):
    rank={}
    for word in sentence.split():
        for letter in word:
            if(letter.isdigit()):
                rank[letter]=word

    return " ".join([rank[x] for x in sorted(rank)])

def order(sentence):
    return " ".join(sorted(sentence.split(), key=lambda x: int(filter(str.isdigit, x))))


def first_non_repeating_letter(string):
    if(len(string)==0):
        return ""
    else:
        out=[le for le in string if string.lower().count(str(le).lower())<2]
        
        
        return "" if len(out)==0 else out[0]


def countBits(n):
    print(bin(n))
    print([int(x) for x in bin(n)[2::]])
    return sum([int(x) for x in bin(n)[2::]])

def countBits(n):
    return bin(n).count("1")


