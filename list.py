list =[1,2,3,4,5]
print(list)

list.append(60)
print(list)

list.insert(3,40)
print(list)

list.remove(5)
print(list)

list.pop(5)
print(list)

list2 = [5,6,7]

list.extend(list2)
print(list)

list[3] = 5
print(list)

list.sort()
print(list)

list.sort(reverse=True)
print(list)

list.reverse()
print(list)

list3 = list.copy()
print(list)

list3.insert (2,[3.1,3.2,3.3])
print(list3)

print(list3[2][2])
