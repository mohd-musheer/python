def fibo(n) : 
    if n==0 :
        return 0 
    elif n==1 :
        return 1
    else :
        return (fibo(n-1)+fibo(n-2))
    

n = int(input("enter number : "))
for i in range(1,n+1) :
    print(fibo(i),end=" ")