L=[10,45,1,67,56]
L.sort()#prints in ascending order
[print(i) for i in L]
L.reverse()#prints in descending order
[print(i) for i in L]
print(L)


s1={100,200,300,400,600}
s2={200,500,600,700,300}
s3=s1.intersection(s2)#prints common elements
s4=s1.symmetric_difference(s2)#prints uncommon elements
s1.remove(400)#removes specified element and prints
print(s1)
print(s3)
print(s4)


T=("john","peter","blessy")
L=list(T)#converts tuple to list
L.append("sweety")#add element to list
L.remove("peter")
T=tuple(L)#convert back to tuple
print(T)

txt=(     "dharshini is a good girl")
x=txt.rfind("is")
changed=txt.replace("d","D")
space=txt.strip()
print(x)
print(changed)
print(space)
x1=txt.rindex("is")
print(x1)

