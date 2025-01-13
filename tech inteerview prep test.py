#1
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
print(arr)
non_zero=0
for i in range (len(arr)):
    if arr[i]!=0:
        arr[non_zero],arr[i]=arr[i],arr[non_zero]
        non_zero+=1
print(arr)


#2
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
print(arr)
zero=0
for i in range (len(arr)):
    if arr[i]==0:
        arr[zero],arr[i]=arr[i],arr[zero]
        zero+=1
print(arr)


#3
n=int(input())
prices=[]
for i in range(n):
    prices.append(int(input()))
max_profit=0
for i in range(1,len(prices)):
    if prices[i]>prices[i-1]:
        max_profit+=prices[i]-prices[i-1]
print("Maximum profit is:",max_profit)
