square=lambda x:x*x
print(square(2))

def myfn(n):
    return lambda x:x*n

double=myfn(2)
print(double(3))

remove_short=lambda lst:list(filter(lambda s:len(s)>5,lst))
words=['apple','orange','banana']
print(remove_short(words))

inc=lambda x:[0.1*x+x if x>1000 else 0.05*x+x]
print(inc(2000))