s=input('Enter string:').split()
max_len = max(len(word) for word in s) 
longest_words = [word for word in s if len(word) == max_len]
if len(longest_words)>=2:
    print('BINGO')
    
else:
    print("word:",longest_words)
