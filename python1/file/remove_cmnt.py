f=False
try:
    f=open('b.txt','r+')
    lines=f.readlines()
    clines=[x for x in lines if not x.strip().startswith('#')]
    f.truncate(0)
    f.seek(0)
    f.writelines(clines)
    print("Removed the comments")
except Exception as e:
    print(e)
finally:
    if f:f.close()