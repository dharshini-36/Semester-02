#1
n=int(input())
num=n**2
if num%n==0:
    print(f"{n} is a Perfect Square")
else:
    print(f"{n} is not a Perfect Square")

#2
num=int(input())
for a in range(1,num+1):
    print('*'.join(str(a) for _ in range(a)))
for a in range(num,0,-1):
    print('*'.join(str(a) for _ in range(a)))

#3
N1=int(input())
N2=int(input())
for i in range(N1):
    for j in range(N2):
        if i==0 or i==N1-1 or j==0 or j==N2-1:
            print("1",end="")
        else:
            print("0",end="")
    print()




