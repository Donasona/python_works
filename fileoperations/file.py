# read file-----

# fr=open("C:\\Users\\donap\\OneDrive\\Attachments\\Desktop\\dev\\python_works\\fileoperations\\data.txt","r")
# for line in fr:
#     print(line)

# write file-----

file_path="C:\\Users\\donap\\OneDrive\\Attachments\\Desktop\\dev\\python_works\\fileoperations\\data.txt"
fw=open(file_path,"w")
# fw.write("hello world")  

# append file-----
 
greetings=["good morning","good afternoon","good evening"]
for g in greetings:
    fw.write(g+"\n")

fa=open(file_path,"a")
food_items=["idiy","tea","dosa"]
for item in food_items:
    fa.write(item+"\n")
