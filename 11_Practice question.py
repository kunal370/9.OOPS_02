'''
define a circle class to create a circle with radius r
using the constructor
define are() method of class which calculates the area of the circle
define parameter() method of the class which allows you to calculate perimeter of the circle

'''

class Circle:
    def __init__(self,radius):
        self.r=radius

    # 3.14*r**2
    def area(self):
        return 3.14*self.r**2

    # 2*3.14*r
    def perimeter(self):
        return 2*3.14*self.r

    def show_all(self):
        print("area is: ",self.area())
        print("perimeter is: ",self.perimeter())


r1=Circle(7)
r1.show_all()

'''
define an Employee class with attributes role, department &salary.
this class also has showdetails() method

create an engineer class that inherits  properties from employee and has
additional attributes : name and age

'''


class Employee:
    def __init__(self,role, department,salary):
        self.rol=role
        self.dept=department
        self.sal=salary

    def showdetails(self):
        print("role is: ",self.rol,"\ndepartment is:",self.dept,"\nsalary is:",self.sal)



class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","IT","359900")


engg1=Engineer("elon musk",40)
engg1.showdetails()
