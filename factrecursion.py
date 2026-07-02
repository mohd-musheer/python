def factorial(n) :
    
    if n==1 :
        return 1

    return n*factorial(n-1)

n = int(input("enter a number : "))
print("factorial is : ",factorial(n))
