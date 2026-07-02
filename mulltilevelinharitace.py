class A :
    def func1(self):
        print("class A")

class B (A):
    def func2(self):
        print("class B")

class C(B):
    def func3(self):
        print("class C")

ob1 = C()
ob1.func1()
ob1.func2()
ob1.func3()