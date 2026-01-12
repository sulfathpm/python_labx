def sum(n):
    if(len(n)==0):return n[0]
    else:
        return n[0]+sum(n[1:])
    
    
n=input("list?")
result=sum(n) 
print(result)