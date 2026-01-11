try:
    n=int(input("Enter a number:"))
    if(n<0): raise ValueError('can\'t be Negative number')
    while n>1 and n%2==0:
        n//=2

    if n==1:
        print('power of 2')
    else:
        print("not a power of 2 ")
except Exception as e:
    print(e)
    