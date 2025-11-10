'''z=int(input('enter number'))
for i in range(0,z+1):
    if(i>1):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            print(i)
'''
z=int(input('numer'))
for i in range(1,z+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)
a=24
b=2
print('%',a%b)

a=12345
b=0
while(a>=1):
    c=a%10
    b=b*10+c
    a=int(a/10)
print(b)



    
