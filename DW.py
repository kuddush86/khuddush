def without(s,n=' '):
    s1=''
    l=[]
    for i in s:
        if i==n:
            l.append(s1)
            s1=''
        else:
            s1+=i
    if s1:
        l.append(s1)
    return l
s='hai hello '
a=without(s)
print(a)
