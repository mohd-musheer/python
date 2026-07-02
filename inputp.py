#Input a number from the user
num=int(input("Enter a number:"))

#Initialize a flag to False
is_even=False

#Use a for loop to check if the number is even
for i in range(2,num+1,2):
    if  i==num:
        is_even=True
        break

#Check the flag to determine if it's even or not
if  is_even:
    print(f"{num} is an even number.")
else:
    print(f"{num} is not an even number.")
