l=['123','345','367','789','333']
l2=[]
for i in l:
    s=''
    for j in i:
        if j!='3':
            s=s+j
    else:
        l2.append(s)
print(l2)
print(s)

l=['hai','hello','fry','why','bye']
l2=[]
for i in l:
    for j in i:
        if j in 'aeiouAEIOU':
            break
    else:
        l2.append(i)
print(l2)

l=['123','345','367','789','333']
l2=[]
for i in l:
    s=''
    for j in i:
        if j!='3':
            s+=j
    else:
        l2.append(s)
print(l2)
print([i.replace('3','') for i in l])





































'''

l=['123','345','367','789','333']
x=[i.replace('3','')for i in l]
print(x)

l=['123','345','367','789','333']
l2=[]
for i in l:
    s=''
    for j in i:
        if j!='3':
            s=s+j
    else:
        l2.append(s)
print(l2)
'''
