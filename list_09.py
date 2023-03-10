def main():
    seq = range(12)
    seq2 = [x * 2 for x in seq]
    from math import pi
    seq3 = {x : x**2 for x in seq}
    print_list(seq)
    print_list(seq2)
    print(seq3)

def print_list(n):
    for x in n: print(x, end = " ")
    print(x)
if __name__ == "__main__" : main()
