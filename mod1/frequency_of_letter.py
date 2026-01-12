# word=input("Enter a word:")
# freq={}
# for ch in word:
#     if ch.isalpha:
#         if ch in freq:
#             freq[ch]=freq[ch]+1
#         else:
#             freq[ch]=1
        
# print(freq)


word=input("Enter word:")
freq={}
for ch in word:
    if ch in freq:
        freq[ch]=freq[ch]+1
    else:
        freq[ch]=1
print(freq)