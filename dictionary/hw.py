# text="this is a python program to find most recursive word this python program is simple"
# display most frequent word

text="this is a python program to find most recursive word this python program is simple"
word=text.split(" ")
wc={}
for w in word:
        if w in wc:
            wc[w]+=1
        else:
              wc[w]=1
print(wc)
srt_wc=sorted(wc,key=wc.get,)
print(srt_wc)
# //screenshot method 2

# max_frequency=0
# max_frequency_dic={}
# for k,v in wc.items():
#     if v > max_frequency:
#         max_frequency=v
#         max_frequency_dic.clear()
#         max_frequency_dic[k]=v
# print(max_frequency_dic)