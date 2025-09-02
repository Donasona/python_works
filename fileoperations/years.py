file_path="C:\\Users\\donap\\OneDrive\\Attachments\\Desktop\\dev\\python_works\\fileoperations\\years.txt"
fr=(file_path,"r")
for yr in fr:
    y=int(yr.strip())
    if(y%4==0 and y%100!=0) or (y%400==0):
        fr.write(y)