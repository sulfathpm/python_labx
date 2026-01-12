from scipy import optimize

f=lambda x:x**2+4*x+4
res=optimize.minimize(f,0)
print(res.x)