l=[]
x=input('enter values with a *space* :\n')
l=x.split()
n=len(l)
e=[]
o=[]
for i in range(n):
	if (int(l[i])%2==0):
		e.append(l[i])
	else:
		o.append(l[i])
print(f'even numbers in list : {e}')
print(f'odd  numbers in list : {o}')