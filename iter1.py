class NumSeries:

   def __init__(self,start , end, inc):
       self.max = end
       self.num = start
       self.inc = inc

   def __iter__(self):
       return self

   def __next__(self):
       self.num = self.num + self.inc
       if (self.num <= self.max):
           return self.num
       else :
           raise StopIteration()

for x in NumSeries(0, 10000000000000000000, 5):
    print (x)


# executing generator -3
x= iter(NumSeries(1,100,2))
while True :
    try:
        print (next(x))
    except StopIteration:
        break