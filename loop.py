print("Odd numbers:",end=" ")
for i in range(1,11):
    if i%2!=0:
        print(i,end=" ")
print("\nEven numbers:",end=" ")
for i in range(1,11):
    if i%2==0:
        print(i,end=" ")
print()

n=input("Enter a string:")
n=n.upper()
reversed_string=""
for i in range(len(n)-1,-1,-1):
    reversed_string+=n[i]
    print("Reversed string:",reversed_string)

