stocks =  {
    "TCS" : 1234.55,
    "INFOSYS": 3444.33,
    "WIPRO" : 544.33
}

print (stocks ["TCS"])
print (stocks.get("WIPRO", "NA"))

stocks ["HCL"] = 200.00
print (stocks)


stocks.update ({"MARUTHI": 6666.99, "TATA": 145.66,
                "WIPRO": 666.55})

print (stocks)

val =stocks.pop ("TCS")
print (val)
print (stocks)

del stocks ["MARUTHI"]
print (stocks)

print (stocks.keys())
print (stocks.values())

for key in stocks.keys():
    print ( stocks[key])

print (stocks.items())

a, b, c = (10,20,88)
for k,v in stocks.items ():
    print (k,v)
