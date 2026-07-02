# def sum () :
#     a = int(input("enter frist numer : "))
#     b = int(input("enter second number : "))
#     sum = a+b
#     print("sum is : ",sum)
#     return

# sum()


# def sum2(x,y):
#     sum = x+y
#     return sum

# a = int(input("enter frist numer : "))
# b = int(input("enter second number : "))
# print("sum is : ",sum2(a,b))

# def sum2(x,y):
#     sum = x+y
#     return sum

# a = int(input("enter frist numer : "))
# b = int(input("enter second number : "))
# print("sum is : ",sum2(x=5,y=8))

# def sum2(x,y=0):
#     sum = x+y
#     return sum

# a = int(input("enter frist numer : "))
# b = int(input("enter second number : "))
# print("sum is : ",sum2(a))


def sumallno(*args) :
    sum =0
    for i in args :
        sum+=i
    return sum

num = sumallno(1,2,3,4,5)
print("sum of all number is ",num)





