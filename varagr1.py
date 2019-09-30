

def add(x, y, *a):
    print (type(a))
    sum = 0
    for x in a :
        sum = sum +x
    return sum + x+ y

#print (add())
#print (add(1))
print (add(1,2))
print (add(1,2,3,4,5,6,7))