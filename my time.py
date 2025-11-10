'''
l=['27','07','1995']
print(l[::-1])

a="2013-12-20 23:40:33"
print(a[::-1])
'''
from datetime import datetime
x=datetime.strptime("2013-12-20 23:40:33", '%Y-%m-%d %H:%M:%S').strftime('%S:%M:%H %d-%m-%Y')
print(x)
e='33:40:23 20-12-2013'
print(len(e))

w=e[15]+e[16]+e[17]+e[18]+'-'+e[12]+e[13]+'-'+e[9]+e[10]+' '+e[6]+e[7]+':'+e[4]+e[3]+':'+e[1]+e[0]
print(w)
