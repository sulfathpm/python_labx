s=input('enter a string:').split()
if len(s)<2:
     print('')
elif len(s)==2:
    print(s[0]+s[1])
else:
    print(s[0]+s[1]+s[-2]+s[-1])
