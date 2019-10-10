def myfunction():
    yield 1
    yield 2
    yield 3

# executing generator -1
x= iter(myfunction())
print (next(x))
print (next(x))
print (next(x))



# executing generator -2
for x in myfunction():
    print (x)



# executing generator -3
x= iter(myfunction())
while True :
    try:
        print (next(x))
    except StopIteration:
        break

