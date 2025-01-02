#1
class Count:
    def __init__(self,in_str):
        self.in_str=in_str
    def count_alphabet(self):
        count_alpha=0
        for i in self.in_str:
            if i.isalpha():
                count_alpha+=1
        print("Alphabetic Characters:",count_alpha)
    def count_num(self):
        count_num=0
        for i in self.in_str:
            if i.isnumeric():
                count_num+=1
        print("Numeric Characters:",count_num)
    def count_sc(self):
        count_sc=0
        for i in self.in_str:
            if i in"!@#$%^&*()_+-?/.":
                count_sc+=1
        print("Special Characters:",count_sc)

user=input("Enter a string: ")
c=Count(user)
c.count_alphabet()
c.count_num()
c.count_sc()


#2
class Validate:
    def __init__(self,in_str):
        self.in_str=in_str
    def validate_string(self):
        sc="!@#$%^&*()_+-=."
        count_sc=0
        count_alpha=0
        for i in self.in_str:
            if i.isalpha():
                count_alpha+=1
            if i in sc:
                count_sc+=1
            if not i.isalpha() and i not in sc:
                return "String must contain 1 alphabet and 1 special character"
            
        if count_alpha<1:
            return "String must contain atleast one alphabet"
       
        if count_sc<1:
            return "String must contain atleast one special character"
        
        return "The string contains both alphabets and special characters."

user=input("Enter a string: ")
val=Validate(user)
print(val.validate_string())


    
        
