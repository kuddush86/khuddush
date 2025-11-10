s='my name is khuddush'
l=[]
a=s.split()
for i in range(len(a)):
    z=a.pop()
    l.append(z)
x=' '.join(l)
print(x)
   
s='my name is khuddush'
l=[]
a=s.split()[::-1]
print('akk',a)
print(s)
print(' '.join(a))

   
s='my name is khuddush'

a=' '.join(s.split()[::-1])
print(a)
