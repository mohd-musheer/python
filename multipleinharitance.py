class father :
    def func1(self):
        print("father class ")

class mother :
    def func2(self):
        print("mother class ")

class child (father,mother):
    def func3(self):
        print("child class ")

ob1 = child()
ob1.func1()
ob1.func2()
ob1.func3()