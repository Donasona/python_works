# st1={10,20,30}
# st2={100,10,200,20}
# intersection_set=st1.intersection(st2)
# print(intersection_set)
# union_set=st1.union(st2)
# print(union_set)
# diff_set=st1.difference(st2)
# print(di)

# empty_st=set()
# customer_order={ "tea","dosa","idly"}
# customer_order.add("fresh-lime")
# print(customer_order) 
# seta={10,20,30}
# setb={100,10,200,20,300,30}
# print(seta.issubset(setb))
# print(setb.issuperset(seta))
# synm=seta.symmetric_difference(setb)
# print(synm)

# sachin_friends=["rahul","ganguly","yuvi","zaheer","raina","dhoni","laxman","srinath"]
# dhoni_friends=["rahul","ganguly","yuvi","zaheer","raina","kohli"]

# union=set(sachin_friends).union(dhoni_friends)
# diff=set(sachin_friends).difference(dhoni_friends)
# intersection=set(sachin_friends).intersection(dhoni_friends)
# print("intersection=",intersection)
# print("diff=",diff)
# print("union=",union)

# ware_house={"laptop","mouse","key-board","wifi_adapter","mic","speaker","projector"}
# actual_items={"laptop","mouse","key_board"}
# missing_item=ware_house.difference(actual_items)
# print(missing_item)
# word1="silent"
# word2="listen"
# print(set(word1)==set(word2) and len(word1)==len(word2))
# wrdst1=sorted(word1)
# wrdst2=sorted(word2)
# print(wrdst1==wrdst2)

word1="bcad"
word2="abcd"
word1_sorted=list(word1)
word1_sorted.sort()
print(word1_sorted)
word2_sorted=list(word2)
word2_sorted.sort()
print(word2_sorted)
print(word2_sorted==word1_sorted)

source_word="chicken"
target_word="hen"
print(set(target_word).issubset(source_word))

