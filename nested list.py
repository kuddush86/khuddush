l1=[]
# function used for removing nested
# lists in python using recursion
def hai(l):
    for i in l:
        if type(i)==list:
            hai(i)
        else:
            l1.append(i)
l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
a=hai(l)
print(l1)
l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
l2=[]
for i in l:
    if type(i)==list:
        continue
    else:
        l2.append(i)
print(l2,'l2')

















l2=[]
def hai(l):
    for i in l:
        if type(i)==list:
            hai(i)
        else:
            l2.append(i)

l=[1,[1,2,3],4,[3,4],4]
a=hai(l)
print(l2)





















