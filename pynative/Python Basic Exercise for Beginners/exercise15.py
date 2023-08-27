def exponent(base, exp):
    x = 1
    for y in range(exp):
        x*=base
    return x

print(exponent(5,3))