#1
class Library:
    def __init__(self,b_name,b_author,b_published):
        self.b_name=b_name
        self.b_author=b_author
        self.b_published=b_published
    def displayLibraryDetails(self):
        print(f"Book Name:{self.b_name}\nBook Author:{self.b_author}\nBook Published on:{self.b_published}")

class Member:
    def __init__(self,member_id,member_name,return_date):
        self.member_id=member_id
        self.member_name=member_name
        self.return_date=return_date
    def displayMemberDetails(self):
        print(f"Member ID:{self.member_id}\nMember Name:{self.member_name}\nBook Return Date:{self.return_date}")
class LibraryManagement(Library,Member):
    def __init__(self,b_name,b_author,b_published,member_id,member_name,return_date):
        super().__init__(b_name,b_author,b_published)
        Member.__init__(self,member_id,member_name,return_date)
    def displayLibraryManagement(self):
        self.displayLibraryDetails()
        self.displayMemberDetails()

l=LibraryManagement("Tangled: The Story of Rapunzel","Disney Book Group",2010,1736,"Dharshini","5-12-2024")
l.displayLibraryManagement()


#2
class Restaurant:
    def __init__(self,res_name,items):
        self.res_name=res_name
        self.items=items

    def displayResInfo(self):
        print(f"{self.res_name}\nMenu:{self.items}")
        
class Delivery:
    def __init__(self,deliveryper_name,contact):
        self.deliveryper_name=deliveryper_name
        self.contact=contact
    def displayDeliveryInfo(self):
        print(f"Delivery Person:{self.deliveryper_name}\nDelivery Person Contact:{self.contact}")
        
class Order(Restaurant,Delivery):
    def __init__(self,res_name,items,deliveryper_name,contact):
        super().__init__(res_name,items)
        Delivery.__init__(self,deliveryper_name,contact)
    def displayOrder(self):
        self.displayResInfo()
        self.displayDeliveryInfo()
        
d=Order("XYZ","Dosa,Idly,Pizza,Burger","John","8456796531")
d.displayOrder()
    
