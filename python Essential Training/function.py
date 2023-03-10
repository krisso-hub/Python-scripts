# check if number is prime or not

def isPrime(n):
    if n <= 0:
        return False
    for x in range(2, n):
        if n % 2 == 0:
            return False
    else:
        return True
# list of prime number from 2 to any number
def listPrime():
    for n in range(50):
        if isPrime(n):
            print(n, end= " ")
    print(n)
listPrime()

# check if any given number is a prime number

n = 4
if isPrime(n):
    print(f"The number {n} is a prime number")
else:
    print(f"the number {n} is not a prime number")
