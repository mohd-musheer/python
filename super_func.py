class A:
    def display(self):
        print("class A")

class B(A):
    def display(self):
        super().display()
        print("class B")

ob1 = B()
ob1.display()