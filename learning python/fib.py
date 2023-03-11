
def fib(n):
    if (n <= 1):
        return n
    else:
        return fib(n -1) + fib(n- 2)

for x in range(10):
    print(fib(x))

def fib():
    first = 0
    second =1
    while True:
        first, second = second, first + second
        yield first

y = fib()
for x in y:
    print(x)
    if x > 30:
        break

def generator(n):
    if n % 2 == 0:
        print("even :" + str(n))
    else:
        print("old:" + str(n))
for x in range(20):
    generator(x)
