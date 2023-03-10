# while loop

words = ["one", "two", "three", "four", "five", "six"]
n = 0
while n < 5:
    print(words[n])
    n += 1
# number doubling series
a, b = 0, 2
while b < 800:
    print(b, end= " " )
    a, b = b, b + b
