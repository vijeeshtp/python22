fruits = {"apple", "banana", "cherry"}

for x in fruits:
  print(x)

print(len(fruits))

print("banana" in fruits)

fruits.add("mango")

fruits.update(["orange", "mango", "grapes"])

fruits.remove("banana") # raise error if item not there

fruits.discard("banana") # NOT rise error

x = fruits.pop()# can not say which item get deleted

fruits.clear()

x = fruits.copy()

x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print ("Z", z)
x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}
w = {"w1", "w2", "w3"}
result = x.union(y, z, w)
print (result)

