#occurance of word
word=input("enter the word to know its occurance::")
string=input("enter the string:")
lst=string.split()
print(lst)
count=0
for i in lst:
    if i==word:
        count=count+1
print(count)
