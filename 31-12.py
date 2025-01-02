#1
import math
def factorial(n):
    if n<=0:

        return "Number should be greater than 0"
    else:
        su=0
        for i in range(1,n+1):
            su+=math.factorial(i)
        return su
num=int(input("Enter the number:"))
print(f"The sum of factorials is: {factorial(num)}")


#2
def fibonacci(n):
    n1=0
    n2=1
    print(n1)
    print(n2)
    for i in range(n+1):
        n3=n1+n2
        n1=n2
        n2=n3
        print(n3)
        if n3>n:
            print(f"First Fibonacci number greater than {n}: {n3}")
            break
n=int(input("Enter the threshold: "))
fibonacci(n)

#3
sentence=input("Enter a sentence: ")
n1=sentence.split()

n=[]
for i in n1:
    n.append(len(i))
    s=sorted(n)
print(s)
a=s[-1]
for i in n1:
    if len(i)==a:
        print(f"Longest word: '{i}' with length {a}")



#
boys=['Virat','Vijay','Vikram','SK','Surya']
for boy in boys:
    try:
        response=input(f"YYYY proposes to {boys}. Do you accept? (yes/no):")
        if response.lower()=="yes":
            print(boy,"Let's go to cage")
            break
        else:
            raise Exception("It's his loss,let's try another boy")
    except Exception as e:
        print(e)
