s='5uygugfu778gyuufyu45ersres8.95cfuodty'
import re
p=r'\d+\.?\d*'
a=re.findall(p,s)
print(a)

'''s='aaaabbbccc'
s1=''
c=1
for i in s:
    if s[i]==s[i+1]:
        c+=1
    else:
        s1+=c
        s1+=s[i]
        c=1
print(s1)
'''
s='aaaabbbcccaa'
d={}
for i in s:
    d[i]=s.count(i)
print(d)
for i in d:
    print((i)+str(d[i]),end='')


'''
s='aaaabbbcccaa'
d={}
for i in s:
    d[i]=s.count(i)
print('d',d)
for i in d:
    print(i+str(d[i]),end='')


s='5uygugfu778gyuufyu45ersres8.95cfuodty'
import re
p=r'\d+\.?\d*'
print(re.findall(p,s))

'''

















    
