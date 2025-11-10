s='shaik mohamad khuddush'
d={}
for i in s:
    d[i]=s.count(i)
print(d)

import re
s='shaik mohamad khuddush'
d1={}
for i in s:
    a=len(re.findall(i,s))
    d1[i]=a
    print(a)
print(d1)

    
s='shaik mohamad khuddush'
d2={}
for i in s:
    sum1=0
    for j in range(len(s)):
        if(s[j])==i:
            sum1+=1
            d2[i]=sum1
print(d2)
