import random
def outer (a, b):

    r= random.randint(1,100000)
    print (r)

    def inner ():
        print (a+b+r)

    return inner

x1= outer (10,20)
x2= outer (5,5)
x3= outer (2,2)

x2()

print (x2.__closure__[0].cell_contents)
print (x2.__closure__[1].cell_contents)
print (x2.__closure__[2].cell_contents)


