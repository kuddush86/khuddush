s='shaik mohamad khuddush'
b=''
for i in s:
    if i not in b:
        b=b+i
        c=s.count(i)    
        print(i,c)
'''
d={}
for i in s:
    d[i]=d.get(i,0)+1
print(d)

import re
d1={}
for i in s:
    c=len(re.findall(i,s))
    d1[i]=c
print(d1)

d2={}
for i in s:
    a=0
    for j in range(len(s)):
        if s[j]==i:
            a+=1
    d2[i]=a
print(d2)
'''

s='shaik mohamad khuddush'
b=''
for i in s:
    if i not in b:
        b=b+i
        c=s.count(i)
        print(i,c)
















