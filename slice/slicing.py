word="pythonprogrammming"
sliced_word= word[:6]
print(sliced_word)
sliced_word2=word[6:]
print(sliced_word2)
sliced_word3=word[::2]
print(sliced_word3)
sliced_word4=word[::-1]
print(sliced_word4)

arr=["word","madom","racecar","car"]
for w in arr:
    if w==w[::-1]:
        print(w)

arr=[10,11,12,13]
for index,element in enumerate(arr):
    print(index,element)

lst=[1,2,3,4,5]
for index,element in enumerate(lst,start=1):
    print(element**index)   