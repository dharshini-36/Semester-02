
balance=int(input("Enter initial balance: "))
while True:
    print("\n1.Deposit\n2.Withdraw\n3.View Balance\n4.Exit")
    operation=int(input("Choose a operation:"))
    match operation:
        case 1:
            deposit=int(input("Enter amount to deposit:"))
            balance+=deposit
            print(f"Amount Deposited: {deposit}. Current balance: {balance}")
        case 2:
            withdraw=int(input("Enter amount to withdraw:"))
            balance-=withdraw
            print(f"Withdrew: {withdraw}. Current balance: {balance}")
        case 3:
            print(f"Current balance: {balance}")
        case 4:
            quit()
        case _:
            print("Please enter correct option")


print("Welcome to D's Hotel")
print("Categories")
print("\n1.Starters\n2.Rotis And Bread\n3.Side dish\n4.Dessert")
option=int(input("Enter your option: "))
match option:
    case 1:
        print("Starters")
        print("1.Paneer 65----------95")
        print("2.Gobi 65-------------80")
        print("3.Honey Baby Corn fry---------120")
    case 2:
        print("Rotis And Bread")
        print("1.Butter Naan--------90")
        print("2.Garlic Naan----------100")
        print("3.Kulcha----------85")
    case 3:
        print("Side dish")
        print("Paneer butter masala----------125")
        print("Gobi manchurian-------------140")
        print("Aloo masala--------------85")
    case 4:
        print("Dessert")
        print("1.Sizzling Brownie--------------105")
        print("2.Chocolate Icecream---------------100")
        print("3.Chocolate Milkshake------------115")
    case _:
        print("THE ITEM IS NOT IN THE MENU")    
