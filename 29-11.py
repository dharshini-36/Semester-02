#multiple inheritance
class Employee:
    def __init__(self,ID,name,position):
        self.ID=ID 
        self.name=name
        self.position=position
    def displayEmployeeInfo(self):
        print(f"Employee ID:{self.ID}\nEmployee Name:{self.name}\nEmployee Position:{self.position}")
        
class Address:
    def __init__(self,street,state,country):
        self.street=street
        self.state=state
        self.country=country
    def displayAddressInfo(self):
        print(f"Street Name:{self.street}\nState:{self.state}\nCountry:{self.country}")
class EmployeeDetails(Employee,Address):
    def __init__(self,ID,name,position,street,state,country):
        super().__init__(name,ID,position)
        Address.__init__(self,street,state,country)
    def displayEmp(self):
        self.displayEmployeeInfo()
        self.displayAddressInfo()

ed=EmployeeDetails("Dharshini",7,"Manager","Shenoy Nagar","Tamil Nadu","India")
ed.displayEmp()


        
