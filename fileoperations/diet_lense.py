file_path = "C:\\Users\\donap\\OneDrive\\Attachments\\Desktop\\dev\\python_works\\fileoperations\\food_logs.csv"
fr = open(file_path,"r")

food_logs=[]

for line in fr:

    data = line.rstrip("\\n").split(",")

    if len(data)>1:

        dictionary ={
            "date":data[0],
            "meal_type":data[1],
            "name":data[2],
            "serving_size":data[3],
            "calories":data[4]
        }

        food_logs.append(dictionary)
        
print(food_logs)

daily_summary ={}

for e in food_logs:

    date = e.get("date")

    calories =int(e.get("calories"))

    if date in daily_summary:

        daily_summary[date]+=calories 

    else:

        daily_summary[date]= calories

print(daily_summary)


        
        