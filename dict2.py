data ={
    "kumar": [22,33,44,55],
    "anil" : [23,33,43,53],
    "kabeer" : [24,34,44,54]
}

for k,v in data.items ():
    total = 0
    for m in v :
        total =total + m
    print (k, total)