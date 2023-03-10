# raising any number to cube
def cube(x):
    return x * x * x

print (cube(2))

# raising a number to any power
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result
    
print (power(3, 3))
print (power(4))

# adding numbers
def multi_add(*args):
    result = 0
    for i in args:
        result = result + i
    return result

print (multi_add(10,2,5,7))