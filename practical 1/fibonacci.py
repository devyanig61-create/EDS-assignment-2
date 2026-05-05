def fibonacci(n):
 if n == 1:
	# write the code..
  return 0
 elif n == 2:
        return 1
 else:
	# write the code..

		return fibonacci( n - 1 ) + fibonacci(n - 2)


n = int(input())
for i in range(1, n + 1):
	print(fibonacci(i), end=" ")
