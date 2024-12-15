l=int(input())
b=int(input())
peri=2*(l+b)
area=l*b
print(f"The required length is {peri}m")
print(f"The required area of carpet is {area}sqm")

a=int(input())#num of copies
b=int(input())#cost per copy
c=int(input())#cost
sold=a*b
printed=a*c
profit=sold-printed-100
print(profit)

n=input()
n=n.strip()#strip white space
print(int(n[0])+int(n[-1]))#sum of the first digit and last digit

num_friends=int(input())
num_teams=int(input())
teams=num_friends//num_teams#with round off
left=num_friends%num_teams#to show reminders
print(f" The number of friends in each team is {teams} and left out is {left}")

p=float(input())
n=float(input())
r=float(input())
interest=(p*n*r)/100
amount=p+interest
discount=(interest*2)/100
final=amount-discount
print(f"{interest:.2f}")
print(f"{amount:.2f}")
print(f"{discount:.2f}")
print(f"{final:.2f}")
