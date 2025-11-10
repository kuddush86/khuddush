#9 convert tuple to dict
t=((1,2),(2,3),(4,5))
t1=(1,2,3,4,5,6)
d={}
print(dict.fromkeys(t1))
print('(1,2)',dict(t))
for i in t1:
    d[i]='a'
print(d)

#10 print sq in dict
d={}
n=int(input('enter number'))
for i in range(1,n+1):
    key=i
    value=i**2
    d[key]=value
print(d)
