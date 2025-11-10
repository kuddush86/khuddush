l=['111','123','145','189','456']
l2=[]
#print([i.replace('1','') for i in l])
for i in l:
    s=''
    for j in i:
        if j!='1':
            s=s+j
        #print(s)

    else:
        l2.append(s)
print(l2)

s='kh udd ush'
l2=[]
s1=''
for i in s:
    if i==' ':
        continue
    else:
        s1+=i
print(s1)
    
