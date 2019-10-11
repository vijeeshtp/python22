def xyz (f):

    def inner (*a, **b):
        print ("---------")
        f (*a, **b)
        print ("---------")
    return inner

@xyz
def hai ():
    print ("Hai")

@xyz
def hello():
    print ("Hello")

@xyz
def add (a,b):
    print ( a+b)

@xyz
def greet (**vals):
    print (vals)
    print ( vals['msg'] +" ," + vals['name'] )


greet (name='kumar', msg= "good morning")

#h =outer (hai)
#h1= outer (hello)
#h ()
#h1()




hai()
hello()
add(11,33)
