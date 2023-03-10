
def Is_even(num):
    if (num % 2 == 0):
        print(num, "is an even number")
    else: 
        print(num, "is an odd number")
Is_even(3)

def main():
    for i in inclusive_range(2, 30, 2):
        print(i, end = ", ")
    print(i)
def inclusive_range(*args):
    numargs = len(args)
    start = 0
    step = 1
if numargs < 1:
    raise TypeError(f"wrong value {numargs}")
elif numargs == 1:
    stop = args[0]
elif numargs == 2:
    (start, stop) = args
elif numargs ==3:
    (start, stop, step) = args
else:
    raise TypeError (f"expected 3 args{numargs}")
i = start
while i <= stop:
    yield i
    i += step
main()