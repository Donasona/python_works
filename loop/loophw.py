
# READ START AND STOP DISPLAY ALL NUMBERS FROM START TO STOP

# start = int(input("enter the starting number:"))
# stop = int(input("enter the ending number:"))
# while (start<=stop):
#     print(start)
#     start+=1

# DISPLAY ALL EVEN NUMBER FROM 1 TO 100

# i=1
# while(i <= 100):
#     if i%2==0:
#         print(i)
#     i+=1

 # DISPLAY ALL ODD NUMBER FROM 1 TO 100

# i=1
# while i <= 100:
#     if i%2!=0:
#         print(i)
#     i+=1
       
# DISPLAY ALL CENTURY YEARS FROM 1879 TO 2026

# year = 1879
# while year <= 2026:
#     if year%100==0:
#         print(year)
#     year+=1

# DISPLAY ALL NON CENTURY YEARS FROM 1879 TO 2026

# year = 1879
# while year <= 2026:
#     if year%100!=0:
#         print(year)
#     year+=1

# DISPLAY ALL LEAP YEARS FROM 1879 TO 2026

# leapyear=1879
# while leapyear<=2026:
#     if leapyear%4==0 and leapyear%100!=0 or leapyear%400==0 and leapyear%100==0:
#         print(leapyear)
#     leapyear+=1    

# DISPLAY THE MULTIPLICATION TABLE OF 8

# i=1
# while i <= 10:
#     result=i * 8
#     print(i,"* 8 =",result)
#     i+=1 

# greetings = "goodmorning"

# message = 'todays, session postponed'

# print(f"{greetings} all {message}")

# greetings = "goodmorning"
# name = "jhon"
# place = "london"
# job_role = "Ai engineer"
# print(f"{greetings} all am {name} from {place} working as a {job_role}")
 
# i=1
# while(i<=10):
#     print(f"{i} * {8} = {i*8}")
#     i+=1

# number = 1875
# while number!=0: #1875   
#     last_digit = number % 10 #1875%10=187.5
#     print(last_digit) #5
#     number = number // 10 #1875//10=187


# set sum
# loop
    # extract last digit
    # add last digit of the number
    # floor
# print sum 

# number = 174
# sum=0
# while number!=0:
#     last_digit = number % 10 
#     sum = sum + last_digit
#     number = number // 10
# print(sum)

# set number 
# set count as 0
# loop
    # extract last_digit
    # increment count by 1
    # remove last_digit
# display count

# num=378640
# count=0
# while num!=0:
#     digit=num%10
#     count+=1
#     num=num//10
# print(count)

# armstrong number

# word="skmckmdkmk"
# cnt = len(word)
# print(cnt)

num=1634
count=len(str(num))
sum=0
while (num!=0):
    digit=num%10
    exponent=digit**count
    sum=sum+exponent
    num=num//10
print(sum) 

