import re
with open('c.txt','r+') as f:
    data=f.read()    
    pattern=r"\b[6-9]\d{9}\b"
    phone=re.findall(pattern,data)
    if phone:
        print("phone no is valid")
        for i in phone:
            print(i)
    else:
        print("invalid no")