'''l=[12,98,34,23,24,13,67,68,34,56,57]
for i in range(len(l)-1):
    a=l[i]+1
    if l[i+1]==a:
        print(l[i],l[i+1])
'''	

l=[12,98,34,23,24,13,67,68,34,56,57]
for i in range(len(l)):
    a=l[i]+1
    print(a)
    for j in range(len(l)):
        if l[j]==a:
            print(l[i],l[j])
               

l=[12,98,34,23,24,13,67,68,34,56,57]
for i in range(len(l)):
    a=l[i]+1
    for j in range(i+1,len(l)):
        if a==l[j]:
            print(l[i],l[j])
