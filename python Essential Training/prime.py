def isprime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
        else:
            return True

n = 5
if isprime(n):
    print(f"{n} is a prime number")
else:
    print("is not")

def listprime(n):
    for n in range(100):
        if isprime(n):
            print(n, end= " ")
    print(n)
listprime(n)