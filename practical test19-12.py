#upper cand lower count
user=input()
lower=0
upper=0
for i in user:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1

print("Count of Upper case Letters:", upper)
print("Count of Lower case letters:", lower)

        
#Factorial of a number

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

num=int(input())
print(f"The Factorial is: {factorial(num)}")


