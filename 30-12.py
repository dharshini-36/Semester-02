
'''import sys
a=[1,2,3]
ref_count=sys.getrefcount(a)
print("Reference count is:",ref_count)


import sys
a=[1,2,3]
b=a
c=b
d=c
print("Reference count is:",sys.getrefcount(a))


import gc #garbage collector module
collected=gc.collect()
print(f"Garbage collector collected {collected} objects")

import gc
l1=[1,2,3]
d1={'a':1,'b':2}
s1="Garbage collection"
del l1
del d1
del s1

collected=gc.collect()
print(f"Garbage Collector collected {collected} objects")'''


import gc
gc.enable()
gc.disable()

l1=[1,2,3]
d1={'a':1,'b':2}
s1="Garbage collection"
del l1
del d1
del s1

#gc.set_threshold(1,2,2)
print('Threshold',gc.get_threshold())
collected=gc.collect()
print(f"Garbage Collector collected {collected} objects")
