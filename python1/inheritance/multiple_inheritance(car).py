class Engine:
    def __init__(self,power=0):
        self.__power=power
    def display(self):
        print("power : ",self.__power)
    
class Wheels:
    def __init__(self,size):
        self.__size=size
    def display(self):
        super().display()
        print("size:",self.__size)

class Car(Wheels,Engine):
    def __init__(self, model=None,power=0,size=0):
        super().__init__(size)
        Engine.__init__(self,power)
        self.__model=model
    def display(self):
        print("Model : ",self.__model)
        super().display()


c1=Car("Tesla model s",500,19)
c1.display()

