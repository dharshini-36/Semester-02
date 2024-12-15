string=input()
string=string.upper()
reversed_string=string[::-1]
print(reversed_string)

n=input()
n=n.upper()
reversed_string=""
for i in range(len(n)-1,-1,-1):
    reversed_string+=n[i]
    print("Reversed string:",reversed_string)
