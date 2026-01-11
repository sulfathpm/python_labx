f=False
try:
    f=open('a.txt','r')
    lines=f.readlines()
    count=len(lines)
    print("Number of lines : ",count)

except Exception as e:
    print(e)

finally:
    if f:f.close()