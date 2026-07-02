class A :
    def __init__ (self,a,b):
        self.a = a
        self.b = b
    
    def display(self):
        print("a = ",self.a)
        print("b = ",self.b)
  
def main():
    ob1 = A(5,10)
    ob1.display()
    
if __name__ == "__main__":
    main()
