s=input("enter string").split()
# max_len=max(len(word) for word in s)
max_len=s.sort()
long_word=len(s[-1])
longest_words=[x for x in s if len(x)==long_word]
print(longest_words)
if((longest_words.count(long_word))>=2):
    print('BINGO')
else:
    print('longest word length:',long_word)