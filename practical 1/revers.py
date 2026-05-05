#write your code here...
num=int(input())
reversed_number=0

while num != 0:
	digit=num % 10
	reversed_number = reversed_number *10 + digit
	num=num//10


print(reversed_number)