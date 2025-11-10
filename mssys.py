# Define the list
#l = ["geeks", "geeks", "for", "geeks"]  # or any other list you want to test
l=['can', 'you',  'can', 'a', 'can', '?']

       #word = can, N = 1

#Output: list - [""you"",  ""can"", ""a"", ""can"" ""?""

# Take user inputs
n = int(input('Enter the occurrence number (n): '))
c = 0
w = input('Enter the word to search for: ')

# Iterate through the list
for i in range(len(l)):
    if l[i] == w:
        c += 1
        print(l[i],c)
    if c == n:
        l = l[i+1:]  # Slice the list starting from the element after the nth occurrence
        break  # Break the loop once we find the nth occurrence

print(l)  # Print the final list

n=int(input('number'))
c=0
w=input('word')
for i in range(len(l)):
    if i==w:
        c+=1
    print(i,c)
    if c==n:
        l=l[i+1:]
        break
print(l)
