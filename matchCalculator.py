n1 = int(input("enter frist number : "))
op = input("enter a operator : ")
n2 = int (input("enter second number :"))

match op :
    case "+":
        print("sum is : ",n1+n2)
    case "-":
        print("sub us : ",n1-n2)
    case "*":
        print("mull is ",n1*n2)
    case "/":
        print("div is ",n1/n2)
    case default  :
        print("invalid opertator")

