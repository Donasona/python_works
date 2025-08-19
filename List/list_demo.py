
# expenses=[10000,12000,13000,14000]
# print(expenses)
# expenses[1]=12500
# print("updated expenses=",expenses)
# totalexpenses=sum(expenses)
# print("total expenses=",totalexpenses)
# highestexpenses=max(expenses)
# print("highest expenses=",highestexpenses)
# avgexpenses=sum(expenses)/len(expenses)
# print("average expenses=",avgexpenses)
# totalexpenses=0
# for i in range(0,len(expenses)):
#     totalexpenses += expenses[i]
# print(totalexpenses)

# attendance = ["H","P","P","P","P","L","H","H","P","P","P","P","L","H"]
# working_days=0
# for a in attendance:
#     if a != "L":
#         working_days+=1
# print(working_days)
# Leave_days=0
# for a in attendance:
#     if a == "L":
#         Leave_days+=1
# print(Leave_days)

# 1
# arr=[1,2,3,4,5,6,7,8,9,10,11,12]
# for i in arr:
#     if i%2==0:
#         print(i)
# 2
# for i in arr:
#     if i%2!=0:
#         print(i)
# 3
# year=[1900,1901,1991,1992,1993,1994,2000,2024,2021,2011]
# for i in year:
#     if i % 4 == 0 and i % 100 != 0:
#         print(i)
#     elif i%400==0 and i%100==0:
#         print(i)
# 4
# def is_armstrong(numbers):
#     sum=0
#     original=numbers
#     digit_count=len(str(numbers))
#     while numbers!=0:
#         digit=numbers%10
#         exponent=digit**digit_count
#         sum+=exponent
#         numbers=numbers//10
#     return sum==original
# numbers=[151,152,153,1634,8891,345,678]
# for num in numbers:
#     if is_armstrong(num):
#         print(num)
# 5
# num=[11,12,13,33,131,343,12321,1234]
# reverse=0
# for i in num:
#     while i>0:
#         digit=i%10
#         reverse=reverse*10+digit
#         i=i//10
#     if reverse==num:
#         print(reverse)
#

# class list:
# def append(object) insert object end of the list

# colors = ["red","green","blue","yellow"]
# colors.append("black")
# print(colors)
# fav_foods="idly vada chaya"
# foods=fav_foods.split()
# foods.append("uzhunuvada")
# print(foods)
# poped_element=colors.pop(2)
# print(colors)
# print(poped_element)
# colors.insert(1,"purple")
# print(colors)
# pos=colors.index("green")
# print(pos)
# occ=colors.count("yellow")
# print(occ)
# colors.reverse()
# print(colors)
# colors.sort()
# print(colors)
# colors.sort(reverse=True)
# print(colors)

# arr=[1,10,11,12,34,35]
# print(arr)
# odd_list=[]
# even_list=[]
# for num in arr:
#     if num%2==0:
#         even_list.append(num)
#     else:
#         odd_list.append(num)
# print(even_list)
# print(odd_list)

# arr1=[10,11,20,17,18]
# arr2=[20,10,12,17]
# for num in arr1:
#     if arr2.count(num)>0:
#         print(num)
    
# for num in arr1:
#     if num in arr2:
#         print(num)

# list=[1,3,4,5]
    # 0 1 2 3 [index]
    #     i j
    # 1 2 3 4 [length]
# for i in range(0,len(list)-1):
#     j=i+1
#     differents=list[j]-list[i]
#     if differents!=1:
#         print(list[i]+1,"is missing")
#         break


                                                                                                                                                                              








