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
# for i in range(2,num):
#     if num%i==0:
#         print("not prime number")
#     else:
#         print("prime number")

num=int(input("enter the number:"))
is_prime=True
for i in range(2,num):
    if num%i==0:
        is_prime=False
        break
    result="prime number" if is_prime==True else "not prime"
    print(result)
# if is_prime==True:
#     print("number is prime number") 
# else:   
#     print("number is not prime number")    
       