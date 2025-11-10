s='shaik mohamad khuddush'
n=''
for i in s:
    if i not in n:
        n=n+i
        b=s.count(i)
        print(i,b)
    
s='shaik mohamad khuddush'
d={}
for i in s:
    sum_=0
    for j in range(len(s)):
        if s[j]==i:
            sum_+=1
    d[i]=sum_
print(d)

d2={}
for i in s:
    d2[i]=d2.get(i,0)+1
print(d2)
    
