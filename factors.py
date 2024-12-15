
#factors of a num
number=int(input())
for i in range(1,number+1):
    if number%i==0:
        print(i,end=" ")

#prime num or not-two factors 1 and and the num itself
#eg:3--1 and 3(factors)
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
#0 1 1 2 3 5 8 13...........n
num_terms=int(input())#5
n1=0
n2=1
count=0
if num_terms<=0:
    print("Enter a positive integer")
elif:
    while count<num_terms:#0<5|1<5|2<5|3<5|4<5|5<5
        print(n1,end=" ")#0|1|1|2|3
        n3=n1+n2#1|2|3|5|8
        n1=n2#n1=1|1|2|3|5
        n2=n3#n2=1|2|3|5|8
        count+=1#1|2|3|4|5
else:
    print("Invalid")






























            
