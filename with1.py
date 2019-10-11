class MyObject:
   def __init__(self):
       print ("Object created")

   def __enter__(self):
      print ("Entered")
      return self

   def __exit__(self ,exc_type, exc_value, tb):
       print ("Exited")

   def mytest1(self):
       print ("aaaaaa")

   def mytest2(self):
       print("bbbbb")


with MyObject () as o:
   o.mytest1()
   o.mytest2()
