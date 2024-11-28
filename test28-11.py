class Inventory:
    def __init__(self,prodID,prodName,prodCount):
        self.prodID=prodID
        self.prodName=prodName
        self.prodCount=prodCount
    
    def display(self):
        print(f"Product ID:{self.prodID}\nProduct Name:{self.prodName}\nProduct Count:{self.prodCount}")
Inven=Inventory(1234,"EyeLiner",10)
Inven.display()




class Inventory:
    def __init__(self):
        self.prodID=12345
        self.prodName="EyeLiner"
        self.prodCount=10

class display(Inventory):
    def dis(self):
        print(f"Product ID:{self.prodID}\nProduct Name:{self.prodName}\nProduct Count:{self.prodCount}")
pro=display()
pro.dis()
