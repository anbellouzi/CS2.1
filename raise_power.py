def raise_power(base, power):
    # base case 1
    if power == 0:
        return 1
    # base case 2
    if power == 1:
        return base
    
    return base * raise_power(base, power-1)   # recursive call
    
print("2^2=", raise_power(2, 2))    
print("4^3=", raise_power(4, 3))
print("10^3=", raise_power(10, 3))