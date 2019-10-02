def calcInterest(term, amt, rate):

    res= term*amt/rate/100
    return res


def main ():

    try:
        x = int (input ("Term #"))
        y = int (input ("Amoun#"))
        z = eval(input ("Interest rate#"))
        r = calcInterest(x, y, z)
        print(r)
    except ValueError as e1:
        print("Please provide correct numeric values")
        print(e1)
    except ZeroDivisionError as e2:
        print("Please don't provide zero")
        print(e2)


    except Exception as e :
        print ("Something went wrong!!!")
        print (e)

    else :
        print (" Done from else block ")
    finally:
        print ("Done")






main ()