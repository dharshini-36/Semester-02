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
    
