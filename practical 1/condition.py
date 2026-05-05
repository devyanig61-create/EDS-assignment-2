#write your code here...
n=int(input())
num=n
c=0
while num>0:
	num=num//10
	c=c+1

if c==1:
	s=n**2
	print(s)
elif c==2:
	sq=n**0.5
	print(f"{sq:.2f}")
elif c==3:
	cr=n**(1/3)
	print(f"{cr:.2f}")
else:
	print("Invalid")
