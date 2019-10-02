
def calc (x, a, b ):
    res = x (a,b)
    return res

def add (a,b):
    if a < 10:
        return a+b + 10
    else :
        return a+b

def main():
    num1 = int(input("Enter num1#"))
    num2 = int(input("Enter num2#"))
    opr = input("Enter op::")

    logic = None

    if (opr == "+"):
        logic = lambda x,y : add (x,y)

    elif (opr == "-"):
        logic = lambda x,y : x-y

    elif (opr == "*"):
        logic = lambda x,y : x*y

    elif (opr == "/"):
        logic = lambda x,y : x/y

    else:
        print("Not supported")


    if logic != None:
        print(type(logic))
        res = calc(logic, num1, num2 )
        print(res)


main()
