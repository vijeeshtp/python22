
import time
import logging

logging.basicConfig(filename="test.log", level=logging.DEBUG)

def outer(func):

   def inner (*args, **kwargs):
       s= "func.__name__" + func.__name__+  "*args= " + str (args )+ "**kwargs" + str (kwargs)
       logging.info (s)
       start = time.time()
       result= func (*args,**kwargs)
       end= time.time()
       logging.info("Time taken for {} is {}".format(func.__name__, end-start))
       return result

   return inner


@outer
def hai ():
    print ("Hai")

@outer
def hello():
    print ("Hello")

@outer
def add (a,b):
    print ( a+b)

@outer
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
