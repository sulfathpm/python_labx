f=False
try:
    f=open('a.txt','r+')
    lines=f.readlines()
    n=int(input("Enter the number of line to remove :"))
    if n<1 or n>len(lines):
        print("invalid line number")
    else:
        lines.pop(n-1)
        f.truncate(0)
        f.seek(0)
        f.writelines(lines)
        print("line removed successfully")
except Exception as e:
    print(e)
finally:
    if f:f.close()