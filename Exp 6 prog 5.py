n = int(input("Enter n:"))
fib = lambda a, b: (b, a+b)
a, b = 0, 1
for i in range(n):
    print(a, end = " ")
    a, b = fib(a, b)
