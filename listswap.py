n = int(input ("enter a size of list : "))
list=[]
for i in range(n):
    num = int(input())
    list.append(num)

print(list)
idx1 = int(input("enter a index number 1 : "))
idx2 = int(input("enter a index number 2 : "))

temp = list[idx1]
list[idx1] = list[idx2]
list[idx2] = temp
print(list)