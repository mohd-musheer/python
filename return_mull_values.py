def retmull():
    a = int(input("enter a : "))
    b = int(input("enter b : "))
    sum = a+ b
    sub = a-b
    return sum , sub

sum,sub = retmull()

print("sum is : ",sum)
print("sub is : ",sub)