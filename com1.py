'''
num1 = [1,2,3,4,5,6,7,8,9,10]
num2 = [1,2,3,4,5,6,7,8,9,10]
newlist =[(x,y) for x in num1 if x %2==0 for y in num2 if y%2!=0]
print (newlist)
'''

'''
num1 = [1,2,3,4,5,6,7,8,9,10]
num2 = [1,2,3,4,5,6,7,8,9,10]
newlist ={(x,y) for x in num1 if x %2==0 for y in num2 if y%2!=0}
print (newlist)
print (type(newlist))
'''

'''
num1 = [1,2,3,4,5,6,7,8,9,10]
num2 = [1,2,3,4,5,6,7,8,9,10]
newlist =((x,y) for x in range(0,100000000000000000,5)  for y in range(1,10) )
print (newlist)
print (type(newlist))

for x in newlist:
    print (x)
'''

names = ["kumar", "anil", "tom"]
marks = [33,44,55]

'''
obj = zip (names,marks)
print (obj)
for x, y in obj:
    print (x, y)
'''

mydict = {x:y   for x, y in  zip (names,marks)  }
#print (mydict)


a = range (1,10)
b=filter(lambda x : x % 2 == 0, a)
print (a)
print (b)
for x in b:
    print (x)


dict_a = [{'name': 'kumar', 'mark': 80},
          {'name': 'anil', 'mark': 75},
          {'name': 'tom', 'mark': 66},
          ]

passed= filter(lambda x : x['mark'] > 70, dict_a)

for x in passed:
    print (x)

mylist = [1,2,3,4,5,6,7,8,9,10]
m = map(lambda x : x*2, mylist)
print (m)

for x in m :
    print (x)


names = ["   kumar  ", "  Tom  ", "  Sunny"]
m = map ( lambda  x : x.strip().upper() ,names)
for x in m :
    print (x)