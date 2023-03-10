
animal  = ("bob", "danny", "tinny", "bobo", "bab", )
for pet in animal:
    if pet == "danny": break
    print(pet)

def main():
    n = ("cat", "git", "mit", "bat", "pat")
    kitten(*n)

def kitten(*x):
    for s in x:
        print(s)
   

if __name__ == "__main__" : main()
