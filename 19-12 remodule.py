#re-module

import re
word="Simple regular expression example regular"
result=re.findall("gula",word)
print(*result)

space=re.search('\s',word)
print("\nThe first space is at:",space.start())

