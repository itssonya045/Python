#which is greathest number among them 

num1= int(input("enter your no : " ))
num2 = int(input("enter your no : " ))
num3 = int(input("enter your no : " ))


if(num1 >= num2 and num1 >= num3) :
    print("num1 is greather")
elif(num2 >= num1 and num2 >=  num3) :
    print("num2 is greather")
else :
    print("num3 is greather")