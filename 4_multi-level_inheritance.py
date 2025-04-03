"""
base(parent)
|
derived(child),(parent)
|
derived(child)

when one class(child/derived) derives the properties and methods of another class(parent/base)

class Car:
   ....

class ToyotaCar (Car):
   ....

"""

class Car:
    color="black"
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped...")

class ToyotaCar(Car):
    def __init__(self,brand):
        self.name=brand


class Fortuner(ToyotaCar):
    def __init__(self,car_type):
        self.type=car_type

car1=Fortuner("diesel")
print(car1.type,car1.color)
car1.start()
car1.stop()

"""
this is multilevel inheritance
   _______________
   |  base class |  <-- parent class
   ---------------
         |
        \|/
   _______________
   | derived class|  <--- child class, (parent class)
   ''''''''''''''''
         |
        \|/
   ________________
   | derived class|  <--- child class
   ''''''''''''''''
"""