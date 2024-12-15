a=5
if a%2==0:
    print("even")
else:
    print("odd")

a=-9
if a>0:
    print("Positive")
elif a<0:
    print("Negative")
else:
    print("Zero")

a=89
b=90
c=87
total_score=a+b+c
per=total_score/3
print(total_score)
print(f"{per:.2f}")
print('Eligible' if per>90 else 'Not Eligible')

s=str(input())
if s.isupper():
    print("Uppercase")
elif s.islower():
    print("Lowercase")
else:
    print("combination of both")
