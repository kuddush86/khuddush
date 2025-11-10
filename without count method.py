s='shaikmohamadkhuddush'
b=''
for i in s:
    if i not in b:
        b=b+i
for i in b:
    c=0
    for j in s:
        if i==j:
            c=c+1
    print(i,c,end=' ')
