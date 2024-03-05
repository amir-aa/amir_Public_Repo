def GCD(a,b):
    if b==0:
        return a
    else:
        return GCD(b,a%b)

def GCD3(a,b,c):
    result_ab=GCD(a,b)
    return GCD(result_ab,c)

print(GCD3(60,40,15))
