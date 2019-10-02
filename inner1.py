

def outer ():

    def add (a,b):
        return a+b

    def diff (a,b):
        return a-b


    num1 = int(input("Enter num1#"))
    num2 = int(input("Enter num2#"))
    opr = input("Enter op::")

    if (opr== "+"):
        print (add (num1, num2))
    elif (opr== "-"):
        print (diff(num1, num2))
    else :
        print ("Not supported")

outer ()


