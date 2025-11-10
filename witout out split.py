def string_parts(in_string , n=" "): 
	s1 = "" 
	l = [] 
	for i in in_string : 
		if i == n: 
			l.append(s1) 
			s1 = "" 
		else: 
			s1 += i  
	if s1: 
		l.append(s1) 
	return l 
 
in_string = "For £10 pounds you can get $20, in my dreams!" 
l_string  = string_parts(in_string)  
print(l_string)

def sl(s,n=' '):
    l=[]
    s1=''
    for i in s:
        if i==n:
            l.append(s1)
            s1=''
        else:
            s1+=i
    if s1:
        l.append(s1)
    return(l)
s='hai hellow how are you'
a=sl(s)
print(a)




            








