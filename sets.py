set = {1,2,3,4,5}
print(set)

for i in set:
    print(i,end=" ")

if 4 in set:
    print("\n 4 present in set")

set.add(6)
print(set)

set.remove(1)
print(set)

list= [1,2,3,4]

set.update(list)
print(list)

s1 = {1,2,3,4}
s2 = {4,5,6,7}

s3 = s1.union(s2)
print(s3)

s1.update(s2)
print(s1)