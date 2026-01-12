l1=input("Enter a list:").split()
m=''
for x in l1:
    if(len(x)>len(m)):
        m=x
print("longest word:",m)