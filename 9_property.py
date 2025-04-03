class Student:
    def __init__(self,chem,math,phy):
        self.chemistry=chem
        self.maths = math
        self.physics = phy
        # self.percentage=(self.chemistry+self.maths+self.physics)/3

    # def calculateper(self):
    #     self.percentage = (self.chemistry + self.maths + self.physics) / 3

    @property
    def percent(self):
        return (self.chemistry + self.maths + self.physics) / 3



stu_1=Student(89,67,79)
print(stu_1.percent)

stu_1.physics=86
print(stu_1.physics)
print(stu_1.percent)
