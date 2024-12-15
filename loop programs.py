start=int(input())
end=int(input())
print("Odd numbers: ",end=" ")
for i in range(start,end):
    if i%2!=0:
        print(i,end=" ")
print("\nEven numbers: ",end=" ")
for i in range(start,end):
    if i%2==0:
        print(i,end=" ")
print()

n=input("Enter a string:")
n=n.upper()
reversed_string=""
for i in range(len(n)-1,-1,-1):
    reversed_string+=n[i]
print("Reversed string:",reversed_string)


sales_figures=[150,-20,300,-50,200,-10,400,-30]
successful_sales=0
returns_or_loses=0
for figures in sales_figures:
    if figures>0:
        successful_sales+=1
    else:
        returns_or_loses+=1
print("Number of successful sales:",successful_sales)
print("Number of returns or loses:",returns_or_loses)



