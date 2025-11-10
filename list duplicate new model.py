l=[1,2,47,8,43,2,1,5,8,47,47]
l2=[]
for i in l:
    a=l.count(i)
    if a>1 and i not in l2:
        l2.append(i)
print(l2)



l=[1,2,47,8,43,2,1,5,8,47,47]
l2=[]
for i in l:
    if i not in l2:
        l2.append(i)
print(l2)

l=[1,2,47,8,43,2,1,5,8,47,47]
l2=[]
for i in range(len(l)):
    a=l.pop()
    l2.append(a)
print(l2)
