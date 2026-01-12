d1={1:20,3:23,5:43}
print(d1)
key=int(input("Enter key to search:"))
print('key exist:',key in d1)
d2={2:34,4:45,5:55}
d1.update(d2)
print(d1)
print(sorted(d1))
print(sorted(d1,reverse=True))
print(sorted(d1.values()))
print(sorted(d1.items()))
print(d1.items())
print(d1.keys())
print(d1.values())