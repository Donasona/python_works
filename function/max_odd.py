# num=int(input("enter the number:"))
# while(num!=0):
#     last_digit=num%10
#     if last_digit%2!=0:
#         print(num)
#         break
#     num=num//10


# def max_odd_number(num):
#     while(num!=0):
#         last_digit=num%10
#         if last_digit%2!=0:
#             print(num)
#             break
#         num=num//10
# max_odd_number(4372)

# def odd_even_count(num):
#  odd_count=0
#  even_count=0
#  while num!=0:
#   digit=num%10
#   if digit%2==0:
#    even_count+=1
#   else:
#    odd_count+=1
#   num//=10
# odd_even_count(12345)
  
# def smart_div(num1=10,num2=8):
#     return num1-num2
# print(smart_div(20,8))

# def exponenet(base,power=3):
#     return base**power
# print(exponenet(3))

def is_leap_year(year):
    if year % 100==0 and year % 400==0 or year % 100!=0 and year % 4==0:
        return True
    else:
        return False
print(is_leap_year(2024))
    