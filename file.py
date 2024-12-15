#1
num=int(input())
while num!=0:
    first=num//100
    sec=(num//10)%10
    third=num%10
    reverse=third*100+sec*10+first
    print(reverse)
    break

#2
n=int(input())
rev=0
while n!=0:  #567|56|5|0--failed.....exits the loop
    rem=n%10   #7|6|5
    rev=(rev*10)+rem   #7|(7*100)+6=76|(76*10)+5=765
    n//=10   #56|5|0
print(rev)

#Armstrong number
n=int(input())  #n=153
sum_dig=0
num=n  #num=153
while n!=0: #153|15|1|0----failed
    rem=n%10 #3|5|1
    sum_dig+=(rem**3)  #(0+
    n//=10
if sum_dig==num:
    print("Armstrong number")
else:
    print("Not an armstrong number")

#prime number
n=int(input())
if n<2:
    f=False
else:
    f=True
    for i in range(2,n):
        if n%i==0:
            f=False
            break
    if f:
        print("Prime")
    else:
        print("Not Prime")
#fibanocci series
n_term=int(input())
