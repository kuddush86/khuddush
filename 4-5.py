#4 generate even numbers another tuple
t=(1,2,3,4,5,6,7,8,9,10)
l=[]
for i in t:
    if(i%2==0):
        l.append(i)
print(tuple(l))

#5 concatinate dict
d1={1:10,2:20}
d2={3:30,4:40}
d3={5:50,6:60}
a={}
b={}
d1.update(d2)
d1.update(d3)
print(d1)
l=[d1,d2,d3]
print(l)
for i in l:
    a.update(i)
print(a)
for i in l:
    for j in i:
        b[j]=i[j]
print(b)




