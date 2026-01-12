def replace_first_char(s):
    if len(s)==0: return s
    else:
        return s[0]+s[1:].replace(s[0],'$')
    
s=input("Enter   a str ing:" )
print("after replacing:",replace_first_char(s))
