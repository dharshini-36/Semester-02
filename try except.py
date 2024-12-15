#try with else and finally
try:
    n1=int(input())
    n2=int(input())
    div=n1/n2
except ZeroDivisionError as zde:
    print(zde)
else:
    print(f"Quotient=",{div})
finally:
    print("Exception is handled")

#assert
try:
    x=-1
    assert x>=0 "Only positive values are allowed"
except AssertionError as e:
    print(e)

#3
try:
    x=int(input())
    assert x>=0,"Only positive values are allowed"
except AssertionError as e:
    print(e)
else:
    print("Number=",x)

class CustomError("This is a Custom Error."):
    pass
try:
    raise CustomError("This is a custom Error.")
except CustomError as e"
print(e)

def sqrt(x):
    if x<0:
        raise ValueError("Cannot compute square root for negative number")
    else:
        return x**0.5
try:
    print(sqrt(-10))
except ValueError as e:
    print(e)

#name error
try:
    print(a)
except NameError as e:
    print(e)

#type error
try:
    s="dharshini"
    ans=s/2
except TypeError as e:
    print(e)

#attribute error
try:
    s="dharshini"
    print(s.uppercase())#upper() is the required method
except AttributeError as e:
    
    
    
