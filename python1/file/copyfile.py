f=False
try:
    f=open('b.txt','r')
    data=f.read()
    dest=open('a.txt','w')
    dest.write(data)
    print("file copied successfully.")

except Exception as e:
    print(e)

finally:
    if f:f.close()