def add (a,b ):
    return a+b

def diff (a, b):
    return a-b

def main ():
    num1 = int (input ("Enter num1#"))
    num2 = int (input ("Enter num2#"))
    opr = input ("Enter op::")


    if (opr =="+") :
         logic=add

    elif (opr == "-"):
        logic =diff
    else :
         print ("Not supported")

    print (type(logic))
    
    res= logic (num1, num2)

    print (res)

main ()

