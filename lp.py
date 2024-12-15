start=int(input())
stop=int(input())
even=[]
odd=[]
for i in range(start,stop):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Even numbers:",even,end="")
print()
print("Odd numbers:",odd,end="")
