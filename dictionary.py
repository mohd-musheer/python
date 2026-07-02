dictionary = {
    "musheer" : 9883483 ,
    "adnan" : 894394,
    "sayam" : 87575
}

print(dictionary)

print(dictionary["musheer"])

print(dictionary.keys())

dictionary["musheer"] = 9370086707
print(dictionary)

dictionary["affan"] = 84756575
print(dictionary)

dictionary.pop("adnan")
print(dictionary)

dictionary.clear()
print(dictionary)

dict1 = {
        "musheer " : 123,
        "ayan" : 8484
}

dict2 = {
        "adnan" : 74745,
        "sayam" : 8484
}

dict1.update(dict2)
print(dict1)


for i in dict1 :
    print(i)

for i in dict1.items() :
    print(i)

for i,j in dict1.items() :
    print(i,j)


#nested dictionary


dict1 = {
    "area1" : {
        "musheer" : 377643,
        "adnan" : 7338783
    },
    "area2" : {
        "saim" : 355745,
        "sayam" : 457387
    }
}

print(dict1["area2"]["sayam"])