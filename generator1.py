def myfunction(s, e, i):

   while (s <= e):
       yield s
       s = s+ i


print (myfunction(1, 100))



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


