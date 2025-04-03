'''
create a class called order which stores item and its price
use dunder function __get__() to convey that:
order1>order2 if price of order1>price of order2

'''

class Order:
    def __init__(self,item,price):
        self.item_name=item
        self.item_price=price


    def __gt__(self,ord2):
        return self.item_price>ord2.item_price

ord1=Order("phone",25999)
ord2=Order("laptop",75999)

print(ord1>ord2)

