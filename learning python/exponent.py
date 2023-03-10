def power(num, x):
    result = 1
    for i in range(x):
        result = result * num
    return result

print(power(3, 3))
