# l=input("Enter a list").split()
# result=[x for x in l if len(x)>6]
# print(result)

l=set(map(int,input("Enter a list").split()))
result=[x for x in l if x>100]
print(result) 