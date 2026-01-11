class FruitBasket:
    def __init__(self,name=None,price=0):
        self.name=name
        self.price=price
    def __add__(self,other):
        if(self.name!=other.name):
            return min(self.price,other.price)

        else:
            return self.price+other.price
        
f1=FruitBasket('apple',22)
f2=FruitBasket('orange',55)
f3=FruitBasket('orange',45)
print(f1+f2,"\n",f2+f3,"\n",f3+f1)