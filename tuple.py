tuple = (1,2,3,4,5)
print(tuple)

print(tuple[2])

print(tuple[0:3])

if 3 in tuple :
    print(" 3 present in tupe ")

for i in tuple :
    print (i,end=" ")

tuple2 = (6,7,8)

tuple = tuple + tuple2
print("\n",tuple)

#unpacking tuple
a,b,c = tuple2
print(a,b,c) 

