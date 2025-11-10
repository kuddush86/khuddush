#1
w=['apple','apple','banana','banana','pear','banana','pear','pear','pear','pear'
   ,'pear']
d={}
for i in w:
    a=w.count(i)
    d[i]=a
print(d)
d1={}
for i in w:
    if i not in d1:
        d1[i]=1
    else:
        d1[i]+=1
print('my',d1)

#2
s='shaik mohamad khuddush'
d={}
for i in s:
    if i in 'aeiouAEIOU':
        a=s.count(i)
        d[i]=a
print(d)
d1={}
for u in s:
    if u in 'aeiouAEIOU':
        d1[u]=s.count(u)
print(d1)
#3 sq 1 to 20 kyes numb values sq
d={}
for i in range(1,21):
    key=i
    value=i**2
    d[key]=value
print(d)
d












