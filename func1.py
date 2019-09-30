def calcInterest(term, amt, rate):
    res= term*amt*rate/100
    return res


def main ():

    x = int (input ("Term #"))
    y = int (input ("Amoun#"))
    z = eval(input ("Interest rate#"))

    r =calcInterest(x, y, z)
    print (r)

main ()