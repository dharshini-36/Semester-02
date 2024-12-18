#1
class Vehicle:
    def __init__(self,name,color,price):
        self.name=name
        self.color=color
        self.price=price
    def show(self):
        print("Details:",self.name,self.color,self.price)
    def max_speed(self):
        print('Vehicle max speed is 150.')
    def change_gear(self):
        print('Vehicle change 6 gear.')
class Car:
    def max_speed(self):
        print('Car max speed is 240')
    def change_gear(Self):
        print('Car change 7 gear')


name=input("Enter the name: ")
color=input("Enter the color: ")
price=int(input("Enter the price: "))

car=Car(name,color,price)
car.show()
car.max_speed()
car.change_gear()

vehicle=Vehicle(name,color,price)
vehicle.show()
vehicle.max_speed()
vehicle.change_gear()




#2
class Library:

    def issue_book(self,book_name,user):
        return f"Book issued: {book_name} to {user}"
    def returned_book(self,book_name,user):
        return f"Book returned: {book_name} by {user}"

class DigitalLibrary(Library):
    def issue_book(self,book_name,user):
        return f"Book issued: {book_name} to {user}"
    def returned_book(self,book_name,user):
        return f"Book returned: {book_name} by {user}"

lib=Library()
dig=DigitalLibrary()

book=input("Enter the book name: ")
username=input("Enter the username: ")

print(lib.issue_book(book,username))
print(lib.returned_book(book,username))
        
print(dig.issue_book(book,username))
print(dig.returned_book(book,username))
        
