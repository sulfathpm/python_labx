with open('a.txt','r') as f:
    lines = f.readlines()

longest = max(lines, key=len)
print("Lengthiest line:", longest.strip())
print("Length:", len(longest))
