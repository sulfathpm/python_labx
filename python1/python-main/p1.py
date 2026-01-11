def replace(s):
    if(len(s)==0):
        return s
    return s[0]+s[1:].replace(s[0],'$')

def swap(s):
    if len(s)>2:
        return s
    return s[-1]+s[1:-1]+s[0]

t=input('text:')
print('replace(result):',replace(t))
print('swap(result):',swap(t))