import random

class Customer:
    def __init__(self,cust_id,name,phno):
        self.cust_id=cust_id
        self.name=name
        self.phno=phno
        
    def gen_rand_id(self):
        c_id=random.randint(1000,9999)
        return f"TICK{c_id}"

    def verify_customer_id(cust_id):
        if cust_id[0:4]=="TICK" and cust_id[4:8].isdigit():
            print("Valid")
        else:
            print("Invalid")

class TicketBooking:
    def __init__(self):
        self.events={"Concert":{"price":1000,"seats":100},
                     "Movie":{"price":150,"seats":200},
                     "Drama":{"price":100,"seats":100}}
        self.booked_tickets=[]
        

    def view_events():
        for events,details in self.events.items():
            print(f"{events}:{details['price']} per ticket {details['seats']} seats are available")
        

    def book_tickets(self,event_name,quantity,customer):
        if event_name in self.events:
            event=self.events[event_name]
            if event['seats']>=quantity:
                totalprice=event['price']*quantity
                event['seats']-=quantity
                self.booked_tickets.append({"customer_id":customer.cust_id,"event":event_name,"quantity":quanity,"Total price":totalprice,})
            else:
                print("Seats not available!!!!!")
        else:
            print("Event name is not available")
    def view_tickets(self,customer):
        print("Ticket Information*")
        cus_ticket=[t for t in self.booked_tickets if t["customer_id"]==customer.cust_id]
        if not cus_ticket:
            print("No Tickets Booked")
        else:
            for tick in cus_ticket:
                print(f"Event:{tick['event']},Quantity:{tick['quantity']},Total Cost:{tick['totalprice']}")

if __name__=="__main__":
    book=TicketBooking()
         
book=TicketBooking()
print("*Welcome to TICKET Booking Application")
cust_id=input("Enter the Customer ID: ")

if Customer.verify_customer_id(cust_id):
    name=input("Enter your name: ")
    phno=int(input("Enter your phone number: "))
    customer=Customer(cust_id,name,phno)
    print("*Booking Details*")
else:
    print("Invalid!!! Please Register")
    name=input("Enter your name: ")
    phno=int(input("Enter your phone number: "))
    cust_id=Customer.gen_rand_id()
    customer=Customer(cust_id,name,phno)
    print("Your Customer ID is:",cust_id)

while True:
    print("*Booking Info*")
    print("\n1.View Events")
    print("\n2.Book Tickets")
    print("\n3.View my Tickets")
    print("\n4.Exit")
    choice=int(input("Enter any option to continue booking: "))
    if choice==1:
        book.view_events()
    elif choice==2:
        event_name=input("Enter any event: ")
        quantity=int(input("Enter the number of tickets: "))
        book.book_tickets(event_name,quantity,customer)
    elif choice==3:
        book.view_tickets(customer)
    elif choice==4:
        exit()
