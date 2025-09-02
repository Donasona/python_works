file_path="C:\\Users\\donap\\OneDrive\\Attachments\\Desktop\\dev\\python_works\\fileoperations\\words.txt"
fw=open(file_path,"w")

words=["hello","hai","madam","racecar","pangram"]
for w in words:
    if w==w[::-1]:
            fw.write(w+"\n")


