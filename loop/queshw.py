


# Write a program that repeatedly sums the digits of a number until a single-digit result is obtained.

# num=int(input("enter the number:"))
# while num>=10:
#     sum = 0
#     if num>0:                      
#             last_digit=num%10
#            it sum=sum+last_digit
#             num=num//10        
# print(sum)        

# Take an integer input and print its reverse using a while loop.

# num=int(input("enter the number:"))
# while num!=0:
#     last_digit=num%10
#     num=num//10
#     print(last_digit)

#  Check whether a number is an Armstrong number using a while loop.

# num=int(input("enter the number:"))
# original=num
# count=len(str(num))
# sum=0
# while num!=0:
#     last_digit=num%10
#     exponent=last_digit**count
#     sum=sum+exponent
#     num=num//10
# if sum==original:
#         print("the number is armstrong")
# else:
#         print("the number is not armstrong")   

#  Use a while loop to generate and print the first n terms of the Fibonacci sequence.

# num=int(input("enter the number of terms:"))
# a=0
# b=1
# c=1
# count=0 dig
# print(f"{a}")
# print(b)
# print(c)
# while count<num:
#     a=b
#     b=c
#     c=a+b
#     count+=1
#     print(c)

# Write a program to count the number of even and odd digits in a given integer.

# num=int(input("enter the number of terms:"))
# even_count=0
# odd_count=0
# while num > 0:
#     digit=num%10
#     if digit%2==0:
#         even_count+=1
#     else:
#         odd_count+=1
#         num=num//10
# print("even digit:",even_count)
# print("odd digit:",odd_count)        
    
#  Create a number guessing game where the user is repeatedly asked to guess a number until they get it right

#  Determine whether a number is a palindrome (reads the same forward and backward) using a while loop

# num=121
# original=num
# reverse=0
# while num!=0:
#     last_digit=num%10
#     reverse=reverse*10+last_digit
#     num=num//10
#     if reverse == original:
#         print("palindrom")
                
# Use a while loop to find the greatest common divisor (GCD) of two numbers using the Euclidean algorithm.

#  Take an integer input and calculate the sum of all its digits using a while loop.

# num=int(input("enter the number:"))
# sum=0
# while num!=0:
#     digit=num%10
#     sum=sum+digit
#     num=num//10
# print(sum)    

#   Use a while loop to print the first n prime numbers.

num1=int(input("enter the number:"))
num2=int(input("enter the number:"))

