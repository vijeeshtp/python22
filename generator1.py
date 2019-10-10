def myfunction():
    yield 1
    yield 2
    yield 3


x= iter(myfunction())
print (next(x))
print (next(x))
print (next(x))


for x in myfunction():
    print (x)


x= iter(myfunction())
while True :
    try:
        print (next(x))
    except StopIteration:
        break

