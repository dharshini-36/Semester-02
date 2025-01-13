#pushing the zero's to end
'''n=int(input())
my_array=[]
for i in range(n):
    my_array.append(int(input()))
zero_dig=[]
new_arr=[]
for i in my_array:
    if i==0:
        zero_dig.append(i)
    else:
        new_arr.append(i)
        
new_arr.extend(zero_dig)
print(*new_arr)

#pushing the zero's to front
n=int(input())
my_array=[]
for i in range(n):
    my_array.append(int(input()))
zero_dig=[]
new_arr=[]
for i in my_array:
    if i==0:
        zero_dig.append(i)
    else:
        new_arr.append(i)
        
zero_dig.extend(new_arr)
print(*zero_dig)

n=int(input())
prices=[]  #7 1 5 3 6 4
for i in range(n):
    prices.append(int(input()))
profit=0
for i in range(1,len(prices)):
    if prices[i]>prices[i-1]: #1>7|5>1|3>5|6>4|
        profit+=prices[i]-prices[i-1]
print(profit)


n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
count=0
for i in arr:
    if arr[i]==0:
        arr.insert(count,pop(i))
'''
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
non_zero=0
for i in range(len(arr)):
    if arr[i]!=0:
        arr[non_zero],arr[i]=arr[i],arr[non_zero]
        non_zero+=1
print("Updated array:",arr)
