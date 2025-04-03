#super method is used to access methods of the parent class

class Car:
    def __init__(self,car_type0):
        self.type=car_type0
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped...")
class ToyotaCar(Car):
    def __init__(self,car_name,car_type1):
        super().__init__(car_type1)
        self.name = car_name
        super().start()


car1=ToyotaCar("Fortuner","electric")
print(car1.type,car1.name)