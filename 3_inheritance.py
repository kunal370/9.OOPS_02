#when one class(child/derived) derives the properties and methods of another class(parent/base)
"""
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
    def __init__(self,car_name):
        self.name=car_name

car1=ToyotaCar("hyrider")
car2=ToyotaCar("Fortuner")

print(car1.name)
print(car1.color)
car1.start()
car1.stop()
  # this is single inheritance
"""
   _______________
   |  base class |  <-- parent class
   ---------------
         |
        \|/
   _______________
   | derived class|  <--- child class
   ''''''''''''''''


"""