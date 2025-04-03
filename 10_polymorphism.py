#when the same operator is allowed to have different meaning according  to the context

#method overloading

class ComplexNumber:
    def __init__(self,real_num,img_num):
        self.real=real_num
        self.img=img_num

    def show_num(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self,new_num):
        newreal=self.real+new_num.real
        newimg=self.img+new_num.img
        return ComplexNumber(newreal,newimg)

    def __sub__(self,new_num):
        newreal=self.real-new_num.real
        newimg=self.img-new_num.img
        return ComplexNumber(newreal,newimg)



num1=ComplexNumber(1,3)
num1.show_num()

num2=ComplexNumber(2,4)
num2.show_num()

num3=num1+num2
num3.show_num()


num3=num1-num2
num3.show_num()
# num3=num1.add_num(num2)
# num3.show_num()