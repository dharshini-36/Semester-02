#1
a=input("Enter First Name:")
name=""
for c in a:
    if  not c.isdigit():
        name+=c
print(f"Hi! Your Entered Input is {name}")


#2
a=input("Enter Name:")
ch=""
sp=""
for c in a:
    if c.isalpha():
        ch+=c
    elif not c.isdigit():
        sp+=c
print(f"Characters: {ch}")
print(f"Special Characters: {sp}")

