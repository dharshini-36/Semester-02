'''
#harshad number
num=int(input()) #54
n1=num
s=0
while num > 0: 
    n=num % 10 #4#5
    s+=n #4#9
    num=num//10 #5
if n1%s==0:
    print(f"{n1} is a Harshad Number")
else:
    print(f"{n1} is not a Harshad Number")
'''
#calculate total number of books
n=int(input())
items=input()
s=items.split(",")
a=0
for i in s:
    dig=int(i)
    a+=dig
print(f"The number of books read by all the students is: {a}")
'''
#right angled triangle of stars
n=int(input())
for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    print()


#method 1
n=int(input())
for i in range(1,n+1):
    print(i*'*')


'''









    
