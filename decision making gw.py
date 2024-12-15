1
a=int(input())
if a%3==0 and a%5==0:
    print("Divisible by both")
elif a%3==0:
    print("Divisible by 3")
elif a%5==0:
    print("Divisible by 5")

2
item1=int(input())
item2=int(input())
item3=int(input())
bill=item1+item2+item3
if bill>400:
    tax=bill*0.0675
    tip=(bill+tax)*0.10
else:
    tax=0
    tip=0
total=bill+tax+tip
import math
tax=math.trunc(tax)
tip=math.trunc(tip)
total=math.trunc(total)
print(bill)
print(tax)
print(tip)
print(total)


3
weight=float(input())
height=float(input())
bmi=(weight/height**2)
print(f"{bmi:.1f}")
if bmi<=16:
    print("severe thinness")
elif bmi>16 and bmi<=17:
    print("moderate thinness")
elif bmi>17 and bmi<=18.5:
    print("mild thinness")
elif bmi>18.5 and bmi<=25:
    print("normal")
elif bmi>25 and bmi<=30:
    print("overweight")
elif bmi>30 and bmi<=35:
    print("obese clss 1")
elif bmi>35 and bmi<=40:
    print("obese class 2")
elif bmi>=40:
    print("obese class 3")
else:
    print("incorrect")


























