data=[1,2,3,4,5,6,7,8,9,100]
data.sort()

def median(lis):
    n=len(lis)
    mid=n//2
    if n%2==0:
        return (lis[mid-1]+lis[mid])/2
    else:
        return lis[mid]
    
q1=median(data[:len(data)//2])
q2=median(data)
q3=median(data[len(data)//2:])

IQR=q3-q1

UF=q3+(1.5*IQR)
LF=q1-(1.5*IQR)

cleaned_data=[x for x in data if LF<=x<=UF]
print("data : ",data)
print('min : ',data[0])
print('max : ',data[-1])
print('Q1 : ',q1)
print('Q2 : ',q2)
print('Q3 : ',q3)


print("UF : ",UF)
print("LF : ",LF)

print('\n\ncleaned data : ',cleaned_data)
Cq1=median(cleaned_data[:len(cleaned_data)//2])
Cq2=median(cleaned_data)
Cq3=median(cleaned_data[len(cleaned_data)//2:])


print('min : ',cleaned_data[0])
print('max : ',cleaned_data[-1])
print('Q1 : ',Cq1)
print('Q2 : ',Cq2)
print('Q3 : ',Cq3)




