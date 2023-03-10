
class myClass():
    def myMethod1(self):
        print("this is my method 1")
    
    def myMethod2(self, somestring):
        print("this is my method 2 " + somestring)


class anothermyClass(myClass):
    def anotherMethod1(self):
        print("this is another method")
    def anotherMethod2(self, something):
        print("this is another method " + something)

def main():
    c = myClass()
    c.myMethod1()
    c.myMethod2("that is sound")
    b = anothermyClass()
    b.anotherMethod1()
    b.anotherMethod2("the second sound")
    b.myMethod1()
    b.myMethod2("is good")


if __name__ == "__main__":
    main()

