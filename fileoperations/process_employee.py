file_path="C:\\Users\\donap\\OneDrive\\Attachments\\Desktop\\dev\\python_works\\fileoperations\\employees.csv"

fr=open(file_path,"r")

all_employees = []

for line in fr:

    line = line.rstrip("\\n")

    data = line.split(",")

    dictionary = {
                  "id" : data[0],"name" : data[1],
                  "department" : data[2],"salary" :data[3],
                  "email":data[4],"location":data[5]
                  }
    all_employees.append(dictionary)

print(all_employees)    

all_employees_names = [e.get("name") for e in all_employees]

ekm_employees = [e.get("name") for e in all_employees if e.get("location") == "ekm"]

print(ekm_employees)

max_sal = max(all_employees,key=lambda e:e.get("salary"))

print(max_sal)

min_sal = min(all_employees,key=lambda e:e.get("salary"))

min_sal_employee = [e.get("name") for e in all_employees if e.get("salary") == min_sal]

print(min_sal_employee)