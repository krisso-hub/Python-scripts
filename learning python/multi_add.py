def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

multi_add(4, 6, 10)
print(multi_add(4, 6, 10))
