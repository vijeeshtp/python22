import datetime

x = datetime.datetime.now()
print(x.year)
print (x.month)
print (x.day)

print (x)

print(x.strftime("%c"))
print(x.strftime("%X"))
print(x.strftime("%x"))
print(x.strftime("%a"))
print(x.strftime("%A"))