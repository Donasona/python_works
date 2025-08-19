# numbers=[1,2,3,4,5,6]
# square_dict={}
# for k in numbers:
#         square_dict[k]=k**2
# print(square_dict)        
    

# for num in numbers:
    # square_dict[num]=num**2
#     square_dict.update({num:num**2})
# print(square_dict)

text="goodmorning"
count={}
# for ch in text:
#     if ch in count:
#         count[ch]+=1
#     else:
#         count[ch]=1
# print(count)

# for ch in set(text):
#     count[ch]=text.count(ch)
# print(count)

set_text=set(text)
print(set_text)
for ch in set_text:
    count_ch=text.count(ch)
    count[ch]=count_ch
print(count)    
# print(max(char_count)) alphabeticaly greater number eduth tharum
max_frequency=0
max_frequency_dic={}#d:1 #o:3
for k,v in count.items():#:k=o v=3
    if v > max_frequency:#3>1
        max_frequency=v#3
        max_frequency_dic.clear()
        max_frequency_dic[k]=v
print(max_frequency_dic)