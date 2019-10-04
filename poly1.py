
from abc import  ABC, abstractmethod

class Car (ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class AltoCar (Car) :

    @abstractmethod
    def start (self):
        print ("starting Alto")

    def accelerate(self):
        print("accelerating Alto")

    def stop(self):
        print("stopping Alto")


class AltoLXI (AltoCar):
    def start (self):
        print ("starting with Key- Alto")



class AltoVXI (AltoCar):
    def start (self):
        print ("starting with button- Alto")

class SwiftCar   (Car):

    def starting (self):
        print ("starting Swift")

    def accelerating(self):
        print("accelerating Swift")

    def stopping (self):
        print("stopping Swift")


    def start(self):
        pass

    def accelerate(self):
        pass

    def stop(self):
        pass



class Person :
    def __init__ (self, name,age):
        self.__name =name
        self._age =age


    def display (self):
        print ("name :", self.__name)
        print ("age :", self.age)

    def setname(self, name):
        self.__name=name

    def drive (self,car):
        car.start()
        car.accelerate()
        car.stop()


a1 = AltoVXI()
s1= SwiftCar()
p1= Person("Anil", 33);
p1.drive(a1)

p1.drive(s1)

