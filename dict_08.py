def main():
    kitten(cat = "meon", dog = "bark ", baby = "cry")

def kitten(**kwargs):
    for s in kwargs:
        print("the animal {} sounds {}".format(s, kwargs[s]))
if __name__ == "__main__" : main()

def main():
    
    y = kitten()
    print(type(y), y )
def kitten():
    print("come")
    return 47
main()