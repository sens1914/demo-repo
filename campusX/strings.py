#1. Find the length of a given string without using the len() function.

# a = input("Enter any string: ")
# count = 0;
# for x in a:
#     count+=1;
# print(f"The length of the string is: {count}")


#2. Extract user name from a given email. eg:- if the email is senda@gmail.com extract only senda.

# email = "senda@gmail.com"
# # pos=email.find("y")  #if there is no 'y' in the given string it will still display the result "senda@gmail.co" but no error will be shown.
# # print(email[:pos])

# pos=email.index("@")   #if there is no 'y' in the given string it won't display the result and error will be shown.
# print(email[:pos])


#3. Count the frequency of a particular character in a provided string.

# string= "hello how are you?"
# print(string.count('h'))


#4. Write a program which can remove a particular characater from a string.

# string= input("Enter the string: ")
# que= input("Which string would you like to remove? ")
# rep= input("With whcich character would you like to replace it? ")
# print(string.replace(que,rep))
 

#5. Write a program that can check whether a given string is pallindrome or not.

# s="racecar"
# left=0
# right=len(s)-1
# flag=True

# while(left<=right):
#     if(s[left]!=s[right]) : 
#             flag=False
#             print("Not a pallindrome")
#             break
#     else : 
#             left+=1
#             right-=1
# if flag:
#        print("Pallindrome")


#6. Write a program to count the number of words in a string without split()

# count = 0
# s="Hi How are you?"
# for i in s:
#     if i==" ":
#         count+=1
# else:
#     print(f"The number of words are : {count+1}")


#7. Write a program to convert a string to title case without using the title().

# s=input("Enter the input : ")
# x=s.split()
# for i in range(len(x)):
#     x[i]=x[i].capitalize()
# x=" ".join(x)
# print(x)
         

#8. Write a program that can convert an integer to string.

x=5
y=str(x)

print(y,type(y))

         

      
        