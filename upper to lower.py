s='Shaik Mohamad Khuddush'
a=s.swapcase()
print(a)
s=''
for i in s:
    if i.isupper():
        s=s+i.ilower()
    elif i.islower():
        s=s+i.isupper()
print(s)
