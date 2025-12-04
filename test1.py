def fibanocci(n):
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
n=int(input(""))
fib=fibanocci(n)
for _ in range(n):
    print(next(fib))
