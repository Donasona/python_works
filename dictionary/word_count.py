# text="hello hai hello hai hai"
# words=text.split(" ")
# # create an empty dictionary
# wc={}
# # exstract each word form words
# for w in words:
#     # add w as key and value as 1 if w not exits update w as current value + 1
#     if w in wc:
#         wc[w]+=1
#     else:
#         wc[w]=1
# print(wc)        

text="ABBAACDAD"
words=text.split(" ")
wc={}
for w in words:
        if w is "A":
            wc[w]+=1
        else:
              wc[w]=1
print(wc)