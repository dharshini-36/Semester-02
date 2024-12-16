#1
word1=input()
word2=input()
merged=[]
i,j=0,0
while i<len(word1) and j<len(word2):
    merged.append(word1[i]) #append 1 char from word 1 and other char from word 2 alternatively
    merged.append(word2[j])
    i+=1 #move to next char
    j+=1 #move to next char
#append remaining characters from longer string
merged.append(word1[i:])
merged.append(word2[j:])
result=''.join(merged) #join the list into string
print(result)
#2
flowerbed=[1,0,0,0,1]
n=int(input())
c=0
length=len(flowerbed)
i=0
while i<length:
    if flowerbed[i]==0:
        pre_emp=(i==0) or (flowerbed[i-1]==0)
        next_emp=(i==length-1) or (flowerbed[i+1]==0)
        if pre_emp and next_emp:
            flowerbed[i]=1
            c+=1
        if c>=n:
            print(True)
            break
    i+=1
if c<n:
    print(False)
