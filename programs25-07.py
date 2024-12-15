
#perfect square
num=int(input())
n=num*num
if n%num==0:
    print(f"{num} is a Perfect Square")
else:
    print(f"{num} is not a Perfect Square")

#pattern
n = int(input())
for i in range(1, n+1):
    print('*'.join(str(i) for _ in range(i)))
for i in range(n, 0, -1):
    print('*'.join(str(i) for _ in range(i)))


#pattern
N1=int(input())
N2=int(input())
for i in range(N1):
    for j in range(N2):
        if i==0 or i==N1-1 or j==0 or j==N2-1:           
            print(" 1 ",end="")
        else:
            print(" 0 ",end="")
    print()


