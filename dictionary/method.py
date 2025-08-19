fruits={"a":"apple","b":"banana","c":"cherry","d":"donut"}
for k in fruits.keys():
    print(k)
poped_value=fruits.pop("d")
print(poped_value)
print(fruits)
get_value=fruits.get("a")
print(get_value)
print(fruits)
all_keys=fruits.keys()
print(all_keys)
all_values=fruits.values()
print(all_values)
for k,v in fruits.items():
    print(k,v)
fruits.update(o ="orange")    
print(fruits)