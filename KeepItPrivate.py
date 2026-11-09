class myClass:

    __privateVar = 77;

    def __privateMethod(self):
        print("I'm inside class myClass")

    def hello(self):
        print("Private variable value :", myClass.__privateVar)


foo = myClass()
foo.hello()
foo.__privateMethod()

