#1
n=int(input())   
a,b=1,1
even_fib=[]
while len(even_fib)<n:
    c=a+b
    a=b
    b=c
    if b%2==0:
        even_fib.append(b)        
print(even_fib[-1])

#2
import math
n_plots=int(input())
areas=list(map(int,input()))
count=0
for area in areas:
    root=math.sqrt(area)
    if int(root)**2==area:
        count+=1
print(count)

