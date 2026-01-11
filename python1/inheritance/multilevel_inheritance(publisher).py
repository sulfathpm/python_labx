class Publisher:
    def __init__(self,name=None):
        self.name=name
    def display(self):
        print("publisher : ",self.name)

class Book(Publisher):
    def __init__(self,name,title=None,author=None):
        super().__init__(name)
        self.title=title
        self.author=author
    def display(self):
        super().display()
        print("author : ",self.author,"\ntitle:",self.title)
    
class Python(Book):
    def __init__(self, name, title, author,price=0):
        super().__init__(name, title, author)
        self.price=price
    def display(self):
        super().display()
        print("price : ",self.price)
b1=Python('anna publictaions','art and the artist','anna',200)
b1.display()