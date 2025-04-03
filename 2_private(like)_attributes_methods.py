class Account:
    def __init__(self,account_no,account_pass):
        self.acc_no=account_no # public attribute
        self.__acc_pass=account_pass # private attribute


    def reset_pass(self):
        print(self.__acc_pass) # we can access private attribute inside the class


acc1=Account("12345","abcd")
print(acc1.acc_no) # we can access this public attribute outside the class
#print(acc1.__acc_pass)  <----  we can not access private attribute outside the class
print(acc1.reset_pass())