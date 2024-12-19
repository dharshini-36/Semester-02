#method overloading 
#2'
'''def addition(a,b):
    c=a+b
    print(c)
addition(4,5)
    
def addition(a,b,c):
    d=a+b+c
    print(d)

#the below line shows error
#addition(4,5)

addition(3,7,5)


# operator overloading

class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
        return self.pages+other.pages

b1=Book(400)
b2=Book(300)
print("Total Number of Pages:",b1+b2)

'''



class Addition:
    def add(self,a,b,c=0):
        result=a+b+c
        return result

ad=Addition()
ans=ad.add(2,3)
print(ans)

ans1=ad.add(1,5,6)
print(ans1)


class Addition:
    def add(self,a,b,c=None):
        if a!=None and b!=None and c==None:
            result=a+b
            return result
        else:
            result=a+b+c
            return result
ad=Addition()
print(ad.add(3,4,9))
