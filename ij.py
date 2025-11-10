
s='shaik mohamad khuddush'
d={}
import re
for i in s:
    a=len(re.findall(i,s))
    d[i]=a
print(d)
