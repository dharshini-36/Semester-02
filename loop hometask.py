#reverse 
n=int(input())
third=n%10
sec=(n//10)%10
first=n//100
reversed_digit=third*100+sec*10+first
print(reversed_digit)
#armstrong number
num=int(input())
sum_powers=0
for digit in str(num):
    sum_powers+=int(digit)**len(str(num))
if sum_powers==num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
