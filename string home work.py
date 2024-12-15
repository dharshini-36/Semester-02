'''
txt="i like cars and my fav car is"
changed=txt.rfind("cars")#searches specified value and returns last position
print(changed)

txt="dharshini"
changed=txt.isidentifier()
print(changed)

txt="dharshini"
changed=txt.islower()#returns true if all char in str are in lower case
print(changed)

num="37"
changed=num.isnumeric()#returns true if all char in str are in number
print(changed)

txt="dharshini"
changed=txt.isprintable()#returns true if all char in str are printable
print(changed)

txt="     "
changed=txt.isspace()#returns true if all char in str are with white space
print(changed)

txt="dharshini"
changed=txt.istitle()#returns true if all char in str follows rules of title
print(changed)

txt="DHARSHINI"
changed=txt.isupper()#returns true if all char in str are in upper case
print(changed)

txt=["john","peter","blessy"]
changed="#".join(txt)#joins the elements
print(changed)

txt=           "dharshini"
changed=txt.ljust(60)#returns left justified version of the str
print(changed)

txt="DHARSHINI"
changed=txt.lower()#converts str into lower case
print(changed)

txt="BMW"
changed=txt.lstrip()#returns left trim version of str
print("of all cars",changed,"is my favourite")

txt="dharshini"
changed=txt.title()#changes the first char to upper case
print(changed)

txt="dharshini"
changed=txt.upper()#converts str into upper case
print(changed)

txt="dharshini"
changed=txt.zfill(10)#fill the str with specified number at the beginning
print(changed)

txt="Hello World"
changed=txt.startswith("Hello")#returns true if str starts with specified value
print(changed)

txt="dharshini"
changed=txt.strip()#returns trimmed version of the str
print(changed)

txt="dharSHINI"
changed=txt.swapcase()#swaps lower case into upper and upper into lower
print(changed)

txt="dharshini"
changed=txt.rjust(30)#returns right justified version of str
print(changed)

txt="dharshini"
changed=txt.rsplit(" , ")#splits the str at specified seperator and returns the str
print(changed)

txt="dharshini"
changed=txt.rstrip()#returns right trimmed version of the str
print(changed)

txt="dharshini"
changed=txt.split("   ")#splits the str at specified seperator and returns the str
print(changed)

txt="Hello\nWorld"
changed=txt.splitlines()#split the str into list
print(changed)

txt="23else"
changed=txt.isidentifier()
print(changed)

txt= "dharshini"
changed=txt.ljust
print(changed)
''

txt="dharshini"
changed=txt.find("girl")
print(changed)

'''
txt="dharshini"
changed=txt.replace("d","D")
print(changed)
'''
