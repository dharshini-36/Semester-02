#harshad number
num=int(input())
num2=int(input())
n1=num
n2=num2
s1=0
s2=0
while num>0:
    n=num%10
    s1+=n
    num=num//10
    while num2>0:
        n=num%10
        s2+=n
        num2=num2//10
if s1%n1==0:
    print(f"{n1} is a Harshad Number")
else:
    print(f"{n1} is not a Harshad Number")
if s2%n2==0:
    print(f"{n2} is a Harshad Number")
else:
    print(f"{n2} is not a Harshad Number")
#2 method      
num=int(input())
n1=num
s=0
while num>0:
    n=num%10
    s+=n
    num=num//10
if s%n1==0:
    print(f"{n1} is a Harshad Number")
else:
    print(f"{n1} is not a Harshad Number")
