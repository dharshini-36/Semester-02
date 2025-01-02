
import gc    #garbage collector module
collected=gc.collect()
print(f"Garbage collecter collected {collected} objects")

import gc
l1=[1,2,3]
d1={'a':1,'b':2}
s1="Garbage collection"
del l1
del d1
del s1

collected=gc.collect()
print(f"Garbage Collector collected {collected} objects")


