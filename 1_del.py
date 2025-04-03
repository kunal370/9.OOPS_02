class Student:
    def __init__(self,stu_name):
        self.name=stu_name

s1=Student("karan")
print(s1.name)
del s1
print(s1.name)
# cause this s1.name is deleted that's why we are getting error





