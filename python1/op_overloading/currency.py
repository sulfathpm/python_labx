class Currency:
    def __init__(self,amt=0,unit=None):
        self.amt=amt
        self.unit=unit
    def __eq__(self, other):
        return ((self.amt==other.amt)and(self.unit==other.unit))
    def display(self):
        print("currency :",self.unit,"amount",self.amt)

c1=Currency('INR',100)
c2=Currency('USD',100)
c3=Currency('INR',100)
if(c1==c2):
    print("c1 is equal to c2")
if(c3==c2):
    print(c3,"is equal to",c2)
if(c1==c3):
    print("c1 is equal to c3")