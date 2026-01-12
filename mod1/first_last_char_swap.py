def swap_first_last_char(s):
    if(len(s)<2):return s
    else:
        return s[-1]+s[1:-1]+s[0]

s=input("Enter a string:")
print("after swap:",swap_first_last_char(s))
