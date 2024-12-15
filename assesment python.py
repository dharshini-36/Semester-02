#vowels count
txt=input()
vowels=0
for char in txt:
    if char.lower() in "aeiou":
        vowels+=1
if vowels>0:
    print(vowels)
else:
    print("No vowels in the entered text")

#count of the digit
num=int(input())
count=len(str(num))
print(count)


