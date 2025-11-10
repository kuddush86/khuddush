l=[1,2,3,4,5,6]
def sqcub(i):
    if(i%2==0):
        return i**2
    else:
        return i**3
r=map(sqcub,l)
print(list(r))
r=(lambda i:i**2 if (i%2==0) else i**3)(7)
print(r)
