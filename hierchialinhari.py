class parant :
    def func1(self):
        print("parant class ")

class child1(parant):
    def func2(self):
        print("child 1")

class child2(parant):
    def func3(self):
        print("child 2")

ob1 = child1()
ob2 = child2()

ob1.func1()
ob1.func2()

ob2.func1()
ob2.func3()