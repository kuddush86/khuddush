import re
'''
a='shaik mohamad khuddush'
d={}
for i in a:
    c=len(re.findall(i,a))
    d[i]=c
print(d)
'''
d={}
a='hai hello how are you'
for i in a:
    s=0
    for j in range(len(a)):
        if a[j]==i:
            s+=1
    d[i]=s
print(d)
'''   
#
a='shaik mohamad khuddush'
d={}
for i in a:
    d[i]=a.count(i)
print(d)
'''

s='shaik mohamad khuddush'
d={}
for i in s:
    a=0
    for j in range(len(s)):
        if s[j]==i:
            a+=1
    d[i]=a
print(d)


a='hai hello how are you'
d={}
s1=''
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for i,j in d.items():
    s1=s1+' '+i+str(j)
print(s1)
    



















