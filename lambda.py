(lambda a:print('even')if a%2==0 else print('odd'))(15)
l=[i**2 for i in range(11)]
print(l)
l=['111','123','145','189','456']
x=[i.replace('1','') for i in l]
print(x)

(lambda a,b:print(a+b))(5,7)

(lambda n:print('even') if n%2==0 else print('odd'))(7)

(lambda a,b:print(a+b))(2,9)

def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return (n*factorial(n-1))
n=5
a=factorial(n)
print('the {} factorial is {}'.format(n,a))



def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return (n*factorial(n-1))
n=6
a=factorial(n)
print('the factorial of {} is {}'.format(n,a))





















