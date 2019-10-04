class Person :
    def __init__ (self, name,age):
        print ("Creating Person")
        self.__name =name
        self._age =age


    def display (self):
        print ("name :", self.__name)
        print ("age :", self.age)

    def setname(self, name):
        self.__name=name

class Student (Person):
    def __init__ (self, name, age, rollno, mark):
        super().__init__(name,age)
        print ("Creating Student")
        self.rollno= rollno
        self.mark =mark

    def display(self):
        super().display()
        print("rollno :", self.rollno)
        print("mark :", self.mark)


s1= Student ("Anil", 23, "1213", 455)
#s1.display()

print (s1.__dict__)

s1.setname("Sunil")

print (s1.__dict__)

s1._Person__name= "Tom"

print (s1.__dict__)

s1._age

#s1.display()
#print (Student.__mro__)


