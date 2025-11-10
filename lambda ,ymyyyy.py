
'''


#(lambda n:print('even') if n%2==0 else print('odd'))(8)

print({i:i**2 for i in range(1,21)if i%2!=0})
print([i**2 for i in range(14)])
print({i:i**2 for i in range(1,21) if i%3==0})

a=[i**2 for i in range(10)]
print(a)


l=[1,2,3,4,5,6,7]
q=list(filter(lambda a:a%2!=0,l))
print(q)



a=list(filter(lambda x:x%2==0,l))
print(a)

s='shaik khuddush'
l=[]
l.extend(s)
for i in l:
    if i in 'aeiou':
        l.remove(i)
a=''.join(l)
print(a)
l=[1,2,3,4,5,6,7]
l1=[]
for i in l:
    if i%2==0:
        l.remove(i)
        l1.append(i)
print(l1+l)


l=[1,2,3,4,5,6,7]
a=list(filter(lambda x:x%2!=0,l))
print(a)


print([i for i in range(11)])
print({i**3:i for i in range(1,11)})



(lambda n:print('even') if n%2==0 else print('odd'))(5)


l=[1,2,3,45,6,7,6,78,5,4,3]
print(list(filter(lambda x:x%2!=0,l)))



a={i**2:i**2 for i in range(10)}
print(a)
'''
s='khu ddu s'
a=str((filter(lambda x:x!=' ',s)))
print(a)
b=''.join(a)
print(b)










