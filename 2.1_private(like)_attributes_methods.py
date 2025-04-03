class Person:
    __name="anonymous" #private attribute

    def __hello(self):
        print("hello person!") #private method

    def welcome(self):
        self.__hello() #calling private method in different public method

p1=Person()
print(p1.welcome()) #calling public method
