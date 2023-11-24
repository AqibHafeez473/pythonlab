#user enter three number 
num1 = int(input("Enter the first number  =  "))
num2 = int(input("enter the second  number  = "))
num3 = int(input("enter the  third number = 10"))

#condition
if num1 >= num2 and num1 >= num3:
 largest= num1
elif num2 >= num1 and num2 >= num3:
    largest= num2
else:
    largest= num3

    print("lagest number is three number =",largest)
