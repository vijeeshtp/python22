def myvals(s, e, i):
    l = []
    while (s <= e):
        l.append( s)
        s = s + i
    return l

def myfunction(s, e, i):
    while (s <= e):
        yield s
        s = s + i


for x in myfunction(0,100000000000000000000000000000000,2):
    print(x)