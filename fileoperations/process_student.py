failed_students="C:\\Users\\donap\\OneDrive\\Attachments\\Desktop\\dev\\python_works\\fileoperations\\failed_student.txt"
all_students="C:\\Users\\donap\\OneDrive\\Attachments\\Desktop\\dev\\python_works\\fileoperations\\all_student.txt"
passed_students="C:\\Users\\donap\\OneDrive\\Attachments\\Desktop\\dev\\python_works\\fileoperations\\passed_students.txt"


f_all_stud_ref=open(all_students,"r")
f_failed_ref=open(failed_students,"r")
f_passed_ref=open(passed_students,"w")

all_stu_set=set()
failed_students_set=set()
for name in f_all_stud_ref:
    all_stu_set.add(name.rstrip("\n"))
print(all_stu_set)
for name in f_failed_ref:
    failed_students_set.add(name.rstrip("\n"))  
print(failed_students_set)  
passed_students_set=all_stu_set.difference(failed_students_set)
print(passed_students_set)
for name in passed_students_set:
    f_passed_ref.write(name+"\n")    
