# ---------------Session on Time Complexity------------

# 1.
# number = int(input('enter the number'))
# digits = '0123456789'
# result = ''  
# while number != 0:
#   result = digits[number % 10] + result
#   number = number//10
# print(result)

# O(log(n))  because number of digits given by user 342 that number of comparison i.e., 3 
            # if one more digit added suppose 3421 then 4 comparison.


# 2. 
# L = [1,2,3,4]

# sum = 0
# for i in L:
#   sum = sum + i
# product = 1
# for i in L:
#   product = product*i
# print(sum,product)

# O(n+n)=O(n)

# 3.
# A = [1,2,3,4]
# B = [5,6,7,8]
# for i in A:
#   for j in B:
#     print(i,j)
    
# O(n**2)


# 4.
# A = [1,2,3,4]
# B = [5,6,7,8]
# for i in A:
#   for j in B:
#     for k in range(1000000):
#       print(i,j)

# O(n*n*1000000)=O(n**2)


# 5.
# L = [1,2,3,4,5]
# for i in range(0,len(L)//2):
#   other = len(L) - i -1
#   temp = L[i]
#   L[i] = L[other]
#   L[other] = temp
# print(L)

# 4 operatins(swapping) and loop running uptill n/2. So, O(4(n/2)). But constants will be removed so answer is O(n). 


# 6.
# n = 10
# k = 0;
# for i in range(n//2,n):
#   for j in range(2,n,pow(2,j)):
#         k = k + n / 2;
# print(k)

# in the second loop need to jump from 2 to 4 to 8 to 16 since pow(2,j) is given... which is an exponential increase
# O(2**n)


# 7.
# a = 10
# b = 3
# if b <= 0:
#   print(-1)
# div = a//b
# print(a-div-b)

# O(1) = constant time since no loop no recursion


# 8.
# n = 345
# sum = 0
# while n>0:
#   sum = sum + n%10
#   n = n // 10
# print(sum)

# O(log(n))  because number of digits given by user 345 that number of comparison i.e., 3 
            # if one more digit added suppose 3451 then 4 comparison.


# 9.
# def fib(n):
#   if n == 1 or n == 0:
#     return 1
#   else:
    # return fib(n-1) + fib(n-2)
  
# O(2**n) in recursion


#10. Subset algorithm

#       {3T(n-1) if n>0
# T(n) = {1, otherwise
 
#     O(3**n) = just put 3T(n-1) repeatetively and at some point put the value ofotherwise i.e., 1


#   {2T(n-1)-1 if n>0
# T(n) = {1, otherwise

#     O(2**n) = just put 2T(n-1)-1 repeatetively and at some point put the value ofotherwise i.e., 1


