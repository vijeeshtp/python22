def add (a,b ):
    return a+b

def diff (a, b):
    return a-b

def main ():
    num1 = int (input ("Enter num1#"))
    num2 = int (input ("Enter num2#"))
    opr = input ("Enter op::")

    if (opr =="+") :
         result = add (num1,  num2)
         print(" sum of {} and {} is {} ".format(num1, num2, result))
    elif (opr == "-"):
        result = diff(num1, num2)
        print(" diff of {} and {} is {} ".format(num1, num2, result))
    else :
         print ("Not supported")

main ()

