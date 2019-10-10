

data = open (file="students.csv", mode ="r+t", encoding='utf-8')
#print (data)
#print (data.read(5))
#print (data.read(10))
#print (data.readline())
#print (data.readline())
#print (data.read())
data.seek(10)
print (data.read(5))

for x in data.readlines():
    print (x)

