a=4
b=5
min=a if a<b else b
print(min)

p=float(input())
r=float(input())
t=float(input())
ci=p*(1+r/100)**t
print(int(ci))


a=3
b=6
a,b=b,a
print(a,b)


L=["paris","bali","singapore","malaysia","switzerland"]
print("paris" in L)

s="python program"
substring="test"
if substring not in s:
    print("true")
else:
    print("false")



