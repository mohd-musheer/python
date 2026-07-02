a = int(input("enter a : "))
b = int(input("enter b : ")) 

try :
    c = a/b
    print(c)
except :
    print("cant devide by zero ....")
else :
    print("else block......")
finally : 
    print("finally block.....")
