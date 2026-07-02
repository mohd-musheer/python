class A:
    def __init__(self,a):
        self.a = a
    
    def __add__(self,o):
        return self.a+o.a

ob1 = A(5)
ob2 = A(5)
print(A.__add__(ob1,ob2))
print(ob1.__add__(ob2))
        