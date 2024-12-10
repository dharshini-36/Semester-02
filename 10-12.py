#1
class Library:
    def __init__(self,b_name):
        self.b_name=b_name
    def displaybook(self):
        print(f"BOOK NAME: {self.b_name}")
        
class Book:
    def __init__(self,b_author,b_published):
        self.b_author=b_author
        self.b_published=b_published
    def displaydetails(self):
        print(f"BOOK AUTHOR: {self.b_author}\nBOOK PUBLISHED ON: {self.b_published}")
        
class Member(Library,Book):
    def __init__(self,b_name,b_author,b_published):
        super().__init__(b_name)
        Book.__init__(self,b_author,b_published)
    def showdetails(self):
        self.displaybook()
        self.displaydetails()
n=input("Enter the book name: ")
a=input("Enter the author name: ")
p=input("Enter the book Published year: ")
l=Member(n,a,p)
l.showdetails()





#2 hybrid
class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def displayEmployeeInfo(self):
        print(f"Name: {self.name}\nAge: {self.age}")

class Manager(Employee):
    def __init__(self,name,age,eid):
        super().__init__(name,age)
        self.eid=eid
    def displayManagerInfo(self):
        self.displayEmployeeInfo()
        print(f"Id: {self.eid}")

class Developer(Employee):
    def __init__(self,name,age,dept):
        super().__init__(name,age)
        self.dept=dept
    def displayDeveloperInfo(self):
        self.displayManagerInfo()
        print(f"Department: {self.dept}")

class TeamLeader(Manager,Developer):
    def __init__(self,name,age,eid,dept,teamsize):
        Employee.__init__(self,name,age)
        self.eid=eid
        self.dept=dept
        self.teamsize=teamsize
    def displayTeamInfo(self):
        self.displayDeveloperInfo()
        print(f"Team Size: {self.teamsize}")
Name=input("Enter name: ")
Age=int(input("Enter age: "))
EID=input("Enter the Employee ID: ")
Dept=input("Enter Department: ")
TS=int(input("Enter Team Size: "))
t=TeamLeader(Name,Age,EID,Dept,TS)
t.displayTeamInfo()
