
#2
'''
n=[1,6,3,7,9,10,10,2,3,7,5]

#remove duplicates:
r=list(set(n))
#or set(n)
print(r)

#sort the list in descending order
s=sorted(n,reverse=True)
print(s)
print()

#3)
#Write a program that takes a number as input and returns the sum of its digits.

number=int(input("Enter the number: "))
s=0
while number>0: #123
    digit=number%10 #3|2|1
    s+=digit #3+2+1
    number//=10 #12|1|
print(s)


#4
#Identify common elements between two lists.

l1=[1,2,3,4,5]
l2=[1,3,7,9,10]
common=[]
for i in l1:
    if i in l2:
        common.append(i)
print(common)


#5
#Write a program that counts the number of words in a given string.
in_str=input("Enter a string: ")
s=in_str.split()
n=len(s)
print(n)


#7
#Create a BankAccount class to simulate a bank account with features:deposit withdraw

class BankAcc:
    def __init__(self,bal):
        self.bal=bal

    def deposit(self,amt):
        if amt>0:
            self.bal+=amt
            print(f"{amt} Amount deposited successfully.. balance:{self.bal}")
        else:
            print("Deposit amount must be positive...")

    def withdraw(self,amt):
        if amt>self.bal:
            print("Insufficient Balance...")
        else:
            self.bal-=amt
            print(f"{amt} Amount withdrawn successfully...balance:{self.bal}")

    def checkbalance(self):
        print(f"Balance: {self.bal}")

        
    
balance=int(input("Enter initial balance: "))
bank=BankAcc(balance)

dep_amt=int(input("Enter amount to deposit: "))
bank.deposit(dep_amt)

with_amt=int(input("Enter amount to withdraw: "))
bank.withdraw(with_amt)


bank.checkbalance()

#6
# Input list from the user
n = list(map(int, input("Enter the elements of the list (space-separated): ").split()))


length = len(n)
for i in range(length):
    for j in range(0, length - i - 1):
        if n[j] > n[j + 1]:
            # Swap elements
            n[j], n[j + 1] = n[j + 1], n[j]

print("Sorted list:",n)

#8
#Check if a given string is a valid email address

import re
def verify_email(email):
    user_mail=r'^[a-z.A-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(user_mail,email))

email=input("Enter the email address: ")

if verify_email(email):
    print(f"{email} is a valid email")
else:
    print(f"{email} is not a valid email")


#9
#Extract all phone numbers from a given text.

text=input()
ph_no=[]
for i in text:
    if i.isdigit():
        ph_no+=i
        print(i,end="")

#10
#Extract all hashtags from a given text.

text=input()
for char in text:
    if char=="#":
        print(char)'''

#1
loginid="DHAR3768"
max_attempts=5
attempts=0

while attempts<max_attempts:
    user_login=input("Enter your login id: ")
    if user_login==loginid:
        print("Login successful")
        break
    else:
        attempts+=1
        remaining_attempts=max_attempts-attempts
        print(f"Incorrect login. you have {remaining_attempts} attempts remaining")

        if attempts==max_attempts:
            print("Account is locked due to too many failed attempts")
            


