f=False
try:
    f=open('a.txt','r')
    words=f.read().split()
    words.sort(key=len,reverse=True)
    l=len(words[0])
    print([x for x in words if len(x)==l])
except Exception as e:
    print(e)
finally:
    if f:f.close()