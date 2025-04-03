class Person:
    name="anonymous"


    '''
    def changename(self,new_name): #normal method or instance method
        self.name=new_name 
    '''
    @classmethod
    def changename(cls,new_name): #class method
        cls.name=new_name

p1=Person()

print(p1.name)
print(Person.name)
p1.changename("Rahul Kumar")
print(p1.name)
print(Person.name)