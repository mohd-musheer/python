class a :
    def take(come,name) :
        come.name=name

    def send(self) :
        return self.name
    
ob1 = a()
ob1.take("musheer")
print(ob1.send())