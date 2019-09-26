vals= [22,33,44,55,66]
print (vals[1])
print (vals[1:])
print (vals[-3:-1])
print (vals[-3:])

print (len (vals))
vals.append("77")
print (vals)

vals.insert (1,15)
print (vals)

vals.remove("77")# object to be deleted
print (vals)
x= vals.pop(1)#index to be deleted
print (x)
vals.reverse()
print (vals)

vals.sort()
print (vals)
vals.extend([88,99,95])
print (vals)

del vals[1]
print (vals)

vals.clear()
print (vals)

del vals
#print (vals)

x=10
del x
print (x)
