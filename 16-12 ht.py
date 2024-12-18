
class User:
    def __init__(self,username,password):
        self._username=username
        self._password=password

    def set_password(self):
        if len(self._password)<8:
            return "Password must be 8 characters long."
        if not any(char.isdigit() for char in self._password):
            return "Password must contain atleast one digit."
        if not any(char in "!@#$%^&*()_+?" for char in self._password):
            return "Password must conatain atleast one special character."
        return "Password is valid."
        
    def check_password(self,input_password):
        return self._password==input_password
   
name=input("Enter your username: ")
password=input("Enter your password: ")
user=User(name,password)

password_validation=user.set_password()
if  password_validation=="Password is valid.":
    input_password=input("Enter your password again: ")
    if user.check_password(input_password):
        print("Password is valid.")
    else:
        print("Password is not valid.")




print()

#2
class Product:
    def __init__(self,name,price,stock):
        self._name=name
        self.set_price(price)
        self.set_stock(stock)
    def set_price(self,price):
        if price>0:
            self._price=price
        else:
            print("Invalid price... Price must be greater than 0")
    def set_stock(self,stock):
        if type(stock) == int and stock >= 0:
            self._stock=stock
        else:
            print("Invalid stock... Stock must be a non negative integer")
    def get_stock(self):
        return self._stock
    def get_price(self):
        return self._price
name=input("Enter the Product name: ")
price=int(input("Enter the price: "))
stock=int(input("Enter the stock: "))
prod=Product(name,price,stock)
prod.set_price(int(input()))
prod.set_stock(int(input()))
print(f"Current Stock: {prod.get_stock()}")

print()

#3
class Student:
    def __init__(self,name,age,marks):
        self.set_name(name)
        self.set_age(age)
        self.set_marks(marks)
    def get_name(self):
        return self._name
    def get_age(self):
        return self._age
    def get_marks(self):
        return self._marks

    def set_name(self,name):
        self._name=name
    def set_age(self,age):
        if 5<= age <=100:
            self._age=age
        else:
            print("Invalid age... Age must be between 5 and 100")
    def set_marks(self,marks):
        if 0 <= marks <=100:
            self._marks=marks
        else:
            print("Invalid marks... Marks must be between 0 and 100")
name=input("Enter your name: ")
age=int(input("Enter your age: "))
mark=int(input("Enter your mark: "))
stu=Student(name,age,mark)
print(f"Name:{stu.get_name()}\nAge:{stu.get_age()}\nMark:{stu.get_marks()}")'''
