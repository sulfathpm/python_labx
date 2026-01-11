l1=input("enter list").split(',')
words=[l1.strip() for l1 in words]
words.sort(key=len)
print("Longest word : ",words[-1])