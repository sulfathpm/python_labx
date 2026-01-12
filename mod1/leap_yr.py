curr_yr=2025
future_yr=int(input("enter a future year?"))
print([x for x in range(curr_yr,future_yr+1) if x%4==0 and x%100!=0 or x%400==0])