# lower_limit=int(input("enter the lowerlimit:"))
# upper_limit=int(input("enter the upperlimit:"))
# for num in range(lower_limit,upper_limit+1):
#     print(num)

# for num in range(10,0,-1):
#     print(num)

# for num in range(50,101):
#     if num % 2==0:
#         print(num)

# prime number

# num=int(input("enter the number:"))
# is_prime=True
# for i in range(2,num):
#     if num%i==0:
#         is_prime=False
#         break
    # result="prime number" if is_prime==True else "not prime"
    # print(result)
# if is_prime==True:
#     print("number is prime number") 
# else:   
#     print("number is not prime number")    
       
# num1=int(input("enter the num1:"))
# num2=int(input("enter the num2:"))
# limit=min(num1,num2)
# gcd=1
# for i in range(1,limit+1):
#     if num1%i==0 and num2%i==0:
#         gcd=i
#         print(gcd)


# from random import randint
# target=randint(1,10)
# attempt=0
# while True:
#     number = int(input(("guess the number:")))
#     attempt+=1
#     if number == target:
#         print(attempt,"times")
#         print("congrats")
#         break

# Input a number n. Using a for loop, find the sum of numbers from 1 to n.

# num=int(input("enter the number:"))
# sum=0
# for i in range(1,num+1):
#     sum=sum+i
#     print(sum)

#  Input a number n. Find the sum of squares from 1^2 + 2^2 + ... + n^2

# num=int(input("enter the number:"))
# square=0
# for i in range(1,num+1):
#     square=square+i**2
#     print(square)

#  Input a number n. Print all even numbers between 1 and n.

# num=int(input("enter the number:"))
# for i in range(1,num+1):
#     if i%2==0:
#         print(i)

# Input a number. Count how many digits it has using a for loop and arithmetic operations

# num=int(input("enter the number:"))
# count=0
# for i in str(num):
#     count+=1
# print(count)



#  Input a number. Reverse it using a for loop and arithmetic (e.g., 123 -> 321)

num=int(input("enter the number:"))
reverse=0
for i in str(num):
    digit=num%10
    reverse=reverse*10+digit
    num=num//10
    if num<0:
        reverse=-reverse
print("reversed number:",reverse)        

#  Input a 3-digit number. Check if it is an Armstrong number using a for loop.

# num=int(input("enter a 3-digit number:"))
# sum=0
# temp=num
# for i in str(num):
#     sum+=int(i) ** 3
#     if sum==num:
#         print("armstrong")
#     else:
#         print("not armstong")

#  Input a number n. Find n! using a for loop.

# num=int(input("enter a number:"))
# factorial=1
# for i in range(1,num+1):
#     factorial*=i
# print(factorial)    


# Input a number. Print all numbers that divide it evenly (i.e., divisors).





# Input a number. Check if it's a prime using a for loop.







# Input two numbers. Find their GCD using a for loop and Euclidean logic.

