def prime(n):
	if n==0:
		return False
	if n==1:
		return False
	for i in range(2,n):
		if n%i==0:
			return False
	return True
l=[]
x=input('enter value ending with *space* :\n')
l=x.split()
n=len(l)
p=[]
c=0
for i in range(0,n):
	if prime(int(l[i])):
		p.append(l[i])
		c=c+1
print(f'prime numbers in list : {p}')
print(f'total number of prime numbers : {c}')