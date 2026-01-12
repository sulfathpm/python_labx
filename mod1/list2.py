l=['ball','apple','Axe','Mirror','Bag']
l.sort()
print("sorted:",l)
l.sort(key=str.lower)
print("sorted-lower:",l)

l.sort(key=len)
print("sorted-length_based:",l)
