vowels_path="C:\\Users\\donap\\OneDrive\\Attachments\\Desktop\\dev\\python_works\\fileoperations\\vowels.txt"
f_vowel_ref=open(vowels_path,"r")
f_vowel_ref_write=open(vowels_path,"w")
vowels=("a","e","i","o","u")
for ch in f_vowel_ref:
    w=ch.strip().lower()
    if w.startswith(vowels):
       print(w)
# for words in w:
#     f_vowel_ref.write(words+"\n")
