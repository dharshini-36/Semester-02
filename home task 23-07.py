#sum of digits 
num=int(input())  #123
s=0
while num>0:
    dig=num%10 #123%10=3| 12%10=2| 1| 0>0....failed
    s+=dig #0+3=3| 3+2=5| 5+1=6
    num=num//10 #123//10=12| 12//10=1| 1//10=0
print(s)


#product of digits
n=int(input()) #543
product=1
while n>0:
    dig=n%10 #543%10=3| 54%10=4| 5|0>0....failed
    product*=dig #1*3=3| 3*4=12| 12*5=60
    n=n//10 #543//10=54| 54//10=5|5//10=0
print(product)

#using for loop decrementing
num=int(input())
for a in range(num,0,-1):
    print(a,end=" ")






