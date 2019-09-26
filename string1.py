s = "Hello World"
print (len (s))
print (s [0:5])
print (s [6:len (s)])
print (s [-11: -6])
print (s [5:])

s = "    Hello World     "
print (s.strip())
print (s.lstrip())
print (s.rstrip())
print (s.upper())
print (s.lower())
print ("World" in s)   
print (s.replace("World", "India"))

data = "123,Kumar,34,55,66,77,55"
vals=data.split(',')
print (vals)
print (vals[0])
print (vals[1])
print (vals[2])
print (vals[3])
print (vals[4])

x= "#".join(vals)
print (x)

a=10
b=20
sum = a+b

s = "Sum of {} and {} is {}".format (a,b,sum)
print (s)

s = "Sum of {aaa} and {y} is {z}".format (z=sum, y=a,aaa=b)
print (s)                                       
