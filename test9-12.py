class StudentMarkManagement:
    def __init__(self,name,rollno,sub1,sub2):
        self.name=name
        self.rollno=rollno
        self.sub1=sub1
        self.sub2=sub2
    def show(self):
        print(f"Name:{self.name}\nRoll No.:{self.rollno}\nSubject 1:{self.sub1}\nSubject 2:{self.sub2}")
class calculate_per_tot(StudentMarkManagement):
    def cal_tot_per(self,name,rollno,sub1,sub2):
        super().__init__(name,rollno,sub1,sub2)
        self.tot=self.sub1+self.sub2
        self.per=(self.tot/200)*100
    def display(self):
        self.show()
        print(f"Total:{self.tot}\nPercentage:{self.per}")
c=calculate_per_tot("Dharshini","E24AI007",80,90)
c.display()
