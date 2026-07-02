
filepath = input("enter a file name : ")
f = open(filepath,"r")
data = f.read()

count = {}
for char in data:
    if char != " ":
        if char in count:
            count[char]+=1
        else :
            count[char]=1
        

for key,value in count.items():
    print(f"{key} : {value}")

print(count)

