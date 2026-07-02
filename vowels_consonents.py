
filepath = input("enter a file name : ")
f = open(filepath,"r")
data = f.read()

vowels = set("AEIOUaeiou")
consonents = set("BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxya")

countV = 0
for v in data:
    if v != " ":
        if v in vowels :
            countV +=1

countC = 0
for c in data:
    if c != " ":
        if c in consonents :
            countC +=1


print("number of vowels is ",countV)
print("number of consonent is ",countC)            

print("number of alphabets and cherector is : ",countV+countC)