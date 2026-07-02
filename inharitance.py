class A:
    def func1(self):
        print("parante class")

class B(A) :
    def func2(self):
        print("child class")


ob1 = B()
ob1.func1()
ob1.func2()