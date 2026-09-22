import math

# -------------------SESSION 1--------------------


#1. "Data","Science","Mentorship","Program"
# "By","CampusX"
# output : Data-Science-Mentorship-Program-started-By-CampusX

# print("Data","Science","Mentorship","Program", sep="-", end="-started-")
# print("By","CampusX", sep="-")


#2. Celsius to Farenheit

# C=int(input("Enter temperature(in Celsius) : "))
# F=(9*C)/5 +32
# print(f"The temperature(in Farenheit) : {F}")


#3. Take two numbers from users and swap thm without using any special python syntax.

# a=int(input("Enter first number : "))
# b=int(input("Enter second number : "))
# a,b=b,a
# print(f"A: {a}")
# print(f"B: {b}")

#  OR

# a=int(input("Enter first number : "))
# b=int(input("Enter second number : "))
# temp=a 
# a=b
# b=temp
# print(f"A: {a}")
# print(f"B: {b}")


#4. Write a program to find the euclidean distance between two coordinates.

# x1=int(input("Enter x1 : "))
# y1=int(input("Enter y1 : "))
# x2=int(input("Enter x2 : "))
# y2=int(input("Enter y2 : "))
# result=round((((x1-x2)**2 + (y1-y2)**2)**0.5), 2)
# print(f"Euclidean distance : {result}")


#5. Write a program to find the simple interest

# p=int(input("Enter the principal amount(in Rs) : "))
# r=int(input("Enter the rate of interset(in percentage) : "))
# t=int(input("Enter the time period(in years) : "))
# SI=(p*r*t)/100
# print(f"Simple Interest : {SI}")
# print(type(SI))   #implicit type conversion happens from int to float.


#6. Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.(Question of linear equation in two variables)
# eg: Input: heads -> 4 legs -> 12     Output : dogs -> 2 chicken -> 2

#Logic ----------- 
#D+C=4
#4D+2C=12
#4D+2(4-D)=12    4D+2(H-D)=12
#4D+8-2D=12      2D=12-2H
#2D=4            D=(12-2H)/2
#D=2             C=H-D

# H=int(input("Enter the total number of heads : "))
# L=int(input("Enter the total number of legs : "))
# D=(12-2*H)/2
# C=H-D
# print(f"Number of dogs : {D}")
# print(f"Number of chickens : {C}")


#7. write a program to find the sum of squares of first n narutral numbers where n will be provided by the user.

# n=int(input("Enter the number of terms : "))
# sum=0
# for i in range(1,n+1):
#     sum+=(i**2)
# print(f"Sum : {sum}")



#8. Given the first 2 terms of an Arithmetic Series. Find the Nth term of the series. Assume all inputs are provided by the user.

# a = int(input("Enter the first term : "))
# b = int(input("Enter the second term : " ))
# n=int(input("Enter the required term : "))
# cd=b-a
# print(f"Required term : {(a+(n-1)*cd)}")

# # OR

# for i in range(3, n+1):
#     b+=cd
# print(f"Required term : {b}")


#9. Given 2 fractions, find the sum of those 2 fractions. Take the numerator and denominator values of the fractions from the user.

# n1 = int(input("Numerator of first fraction : "))
# d1 = int(input("Denominator of first fraction : "))
# n2 = int(input("Numerator of second fraction : "))
# d2 = int(input("Denominator of second fraction : "))
# rn=(n1*d2)+(n2*d1)
# rd=(d1*d2)
# print("Result : {}/{}".format(rn,rd))


#10. Given the height, width and breadth of a milk tank, you have have to find put how many glasses of milk can be obtained? Assume all the inputs are provided by the user.

# l=int(input("Length of tank : "))
# b=int(input("Breadth of tank : "))
# h=int(input("Height of tank : "))
# r=int(input("Radius of glass : "))
# hg=int(input("Height of glass : "))
# vol_tank=l*b*h
# vol_glass=3.14*r*r*hg
# result=math.floor((vol_tank//vol_glass))
# print(type(result))
# print(f"Required glasses can be obtained : {result}")


# -------------------SESSION 2--------------------


#1. Write a  program that will give you the in hand salary after deduction on CTC - HRA(10%), DA(5%), PF(3%) and taxes deduction as below : 
# Salary(Lakhs) : Tax(%)
# Below 5 : 0%
# 5-10 : 10%
# 10-20 : 20%
# above 20 : 30%

# CTC=int(input("Enter the CTC(in RS) :  "))

# HRA= (10*CTC)/100
# DA= (5*CTC)/100
# PF= (3*CTC)/100

# deductions=HRA+DA+PF

# if(CTC>=2000000):
#     tax=(30*CTC)/100
# elif(CTC>=1000000):
#     tax=(20*CTC)/100
# elif(CTC>=500000):
#     tax=(10*CTC)/100
# else : 
#     tax=0

# salary=CTC-tax-deductions
# print(deductions)
# print(tax)
# print(f"In hand salary : Rs{salary:.2f}")


#2. Write a program that takes a user input of three angles and will find out whether it can form a triangle or not.

# first = int(input("Enter the first angle : "))
# second = int(input("Enter the second angle : "))
# third = int(input("Enter the third angle : "))
# if (first+second+third==180 and first>0 and second>0 and third >0):
#     print("It can form a triangle.")
# else : 
#     print("It cannot form a triangle.")


#3. Write a program tat will take the user input of cost price and selling price and determines whether its a loss or profit.

# cost_price=int(input("Enter the cost price : "))
# selling_price=int(input("Enter the selling price : "))

# if(cost_price>selling_price):
#     print("Loss.")
# elif(cost_price<selling_price):
#     print("Profit")
# else:
#     print("Neither loss nor profit")


#4. Write a menu driven program - 
    # 1. cm to ft
    # 2. km to miles
    # 3. USD to INR
    # 4. exit

# option = int(input('''Choose option :
#      1. cm to ft
#      2. km to miles
#      3. USD to INR
#      4. exit
# '''))
# if option==1:
#     num=int(input("Enter the number(in cm) : "))
#     result = num*0.032
#     print(f"Result(in ft) : {result:.3f}")
# elif option==2:
#     num=int(input("Enter the number(in km) : "))
#     result = num*0.62
#     print(f"Result(in miles) : {result:.3f}")
# elif option==3:
#     num=int(input("Enter the number(in USD) : "))
#     result = num*85.53
#     print(f"Result(in INR) : {result:.3f}")
# elif option==4:
#     exit
# else:
#     print("Not a valid option.")


#5. Diplay fibonacci series upto n terms.

# n=int(input("Enter the number of terms : "))
# first=0
# second=1
# print(first, second, sep= " ", end=" ")
# for i in range(2,n):
#     temp=second
#     second=first+second
#     first=temp
#     print(second, sep= " ", end=" ")


#6. Find the factorial of a given number.

# num=int(input("Enter the number for factorial to be calculated : "))
# result=1
# for i in range(num,0,-1):
#     result*=i
# print(f"Result : {result}")


# 7. Reverse a given integer.

# num=int(input("Enter the number to be reversed : "))
# new_num=0
# while num>0:
#     digit=num%10
#     new_num=new_num*10+digit
#     num=num//10
# print(f"Result : {new_num}")


# 8.  Take a user input as integer N. Find out the sum from 1 to N. 
# If any number if divisible by 5, then skip that number. 
# And if the sum is greater than 300, don't need to calculate the sum further more. 
# Print the final result. And don't use for loop to solve this problem.

# num=int(input("Enter the number of terms : "))
# sum=0
# i=1
# while i<num+1:
#     if sum>300:
#         break
#     else :
#         if(i%5==0):
#             i+=1
#             continue
#         else:
#             sum+=i
#             i+=1
# print(f"Result : {sum}")


# 9.  Write a program that keeps on accepting a number from the user until the user enters Zero. Display the sum and average of all the numbers.

# sum=0
# count=0
# while True:
#     n=int(input("Enter the number : "))
#     if(n==0):
#         print(f"Sum : {sum}")
#         print(f"Average : {sum/count}")
#         break
#     else:
#         count+=1
#         sum+=n


#10. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

# L=[]
# for i in range(2000, 3201):
#     if(i%7==0 and i%5!=0):
#         L.append(str(i))
# print(", ".join(L))


# 11. Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number. The numbers obtained should be printed in a space-separated sequence on a single line.

# L=[]
# for i in range(1000, 3001):
#     if(i%2==0):
#         L.append(str(i))
#     else:
#         continue
# print(", ".join(L))


# 12.  A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
# Input
#  UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# !
# Output 2

# up=int(input("Enter upwards motion : "))
# down=int(input("Enter downwards motion : "))
# left=int(input("Enter left motion : "))
# right=int(input("Enter right motion : "))
# vertical=up-down
# horizontal=left-right
# distance=math.floor(((vertical)**2+(horizontal)**2)**0.5)
# print(f"Distance : {distance}")


# 13. Write a program to print whether a given number is a prime number or not.

num = int(input("Enter the number : "))
flag = True

for i in range(2,num):
    if(num%i==0):
        flag=False
        print("Not Prime")
        break
if flag:
    print("Prime")


# 14. Print all the Armstrong numbers in a given range. 


# 15. Calculate the angle between the hour hand and minute hand.
# Note: There can be two angles between hands; we need to print a minimum of two. Also, we need to print the floor of the final result angle. For example, if the final angle is 10.61, we need to print 10.
# Input:
# H = 9 , M = 0
# Output:
# 90
# Explanation:
# The minimum angle between hour and minute hand when the time is 9 is 90 degress.
# This code calculates the angle between the hour and minute hand on a clock. It takes user input for the hour and minute hand positions, validates the input to make sure it is within the range of a clock (0-12 for hours and 0-60 for minutes), then calculates the angles of the hour and minute hand based on their position on the clock. It then finds the difference between the two angles and takes the absolute value of that difference. It then checks if the angle is greater than 180, if it is, it prints the difference of 360 and the angle, else it prints the angle. The final output is the angle between the hands on the clock.


# 16. Given two rectangles, find if the given two rectangles overlap or not. A rectangle is denoted by providing the x and y coordinates of two points: the left top corner and the right bottom corner of the rectangle. Two rectangles sharing a side are considered overlapping. (L1 and R1 are the extreme points of the first rectangle and L2 and R2 are the extreme points of the second rectangle).
# Note: It may be assumed that the rectangles are parallel to the coordinate axis.
# The given code takes the coordinates of two rectangles from the user and checks if they overlap.

# It does this by first checking if either rectangle has an area of 0 (i.e. one of the sides has length 0), in which case it prints "Don't Overlap".
# It then checks if one rectangle is entirely to the left or above the other, in which case it also prints "Don't Overlap". If none of these conditions are true, it prints "Overlap".




