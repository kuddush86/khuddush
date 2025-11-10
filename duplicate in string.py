
s='geeksforgeeks'
d={}
l=[]
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)
for i,j in d.items():
    if j<=1:
        print(i,end=(''))

s='geeksforgeeks'
d={}
l=[]
for i in s:
    d[i]=s.count(i)
print(d)
for i,j in d.items():
    if j>1:
        l.append(i)
a=''.join(l)
print(a)


























