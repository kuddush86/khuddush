s='my name is khuddush'
l=[]
s1=''
for i in s:
    if i==' ':
        l.append(s1)
        s1=''
    else:
        s1+=i
print(l)
if s1:
    l.append(s1)
print(l)

s='my name is khuddush'
import re
print(re.findall(r'\S+',s))
