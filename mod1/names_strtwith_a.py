names=input("Enter a list").split()
count=0
for name in names:
    if name.lower().startswith('a'):
        count+=1
print(count)