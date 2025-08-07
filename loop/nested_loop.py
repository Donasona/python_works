# for row in range(1,5):
#     for col in range(1,4):
#         print(row,end=" ")
#     print(" ")        

# for row in range(1,5):
#     for col in range(1,4):
#         print(col,end=" ")
#     print(" ")   

# for row in range(1,6):
#     for col in range(1,row+1):
#         print(col,end="\t")
#     print()    

# for row in range(1,6):
#     for col in range(1,7-row):
#         print(col,end="\t")
#     print()    

# right half pyramid

# for row in range(1,7):
#     for col in range(1,row+1):
#         print("*",end="\t")
#     print() 

# left half pyramid

# for row in range(1,6):
#     for col in range(1,7-row):
#         print("*",end="\t")
#     print()    

# full pyramid

# for row in range(1,6):
#     for sp in range(1,7-row):
#         print(" ",end="")
#     for col in range(1,row+1):
#         print("* ",end=" ")
#     print()      
 
# Inverted right half pyramid

# for row in range(1,6):
#     for sp in range(1,7-row):
#         print("* ",end="")
#     print()   

# inverted full pyramid

# for row in range(1,6):
#     for col in range(1,row):
#         print(" ",end="")
#     for sp in range(1,7-row):
#         print("* ",end="")
#     print()    

# inverted left half triangle

# for row in range(1,5):
#     for col in range(1,row+1):
#         print(" ",end="")
#     for sp in range(1,6-row):
#         print("*",end="")
#     print()    

# Rhombus pattern //



# diamond pattern

# for row in range(1,6):
#     for sp in range(1,7-row):
#         print(" ",end="")
#     for col in range(1,row+1):
#         print("* ",end=" ")
#     print()  
# for row in range(1,5):
#     for col in range(1,row+1):
#         print(" ",end="")
#     for sp in range(1,6-row):
#         print(" * ",end="")
#     print()  
  
# hourglass pattern

# for row in range(1,5):
#     for col in range(1,row+1):
#         print(" ",end="")
#     for sp in range(1,6-row):
#         print("* ",end="")
#     print()    
# for row in range(2,5):
#     for sp in range(1,6-row):
#         print(" ",end="")
#     for col in range(1,row+1):
#         print("*",end=" ")
#     print()  

# hollow square pattern //

# for row in range(1,5):
#     for col in range(1,row+1):
#         print(" *",end="")
# print()    
# for row in range(1,4):
#     for col in range(1,row+1,4):
#         print(" *",end="\t")
#     print()    
# for row in range(1,5):
#     for col in range(1,row+1):
#         print(" *",end="")
# print()  
   
# floy's triangle

# num=1
# for row in range(1,5):
#     for col in range(row):
#         print(" ",num,end="")
#         num+=1
#     print()