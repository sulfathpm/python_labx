f=False
try:
    f=open('a.txt','r+')
    lines=f.readlines()
    lines.sort(key=len,reverse=True)
    l=len(lines[0])
    print([x for x in lines if len(x)==l])
except Exception as e:
    print(e)
finally:
    if f:f.close()