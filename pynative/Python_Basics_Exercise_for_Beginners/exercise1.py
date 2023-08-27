def f(number1, number2):
    product = number1 * number2
    if product <= 1000:
        return(product)
    else:
        return(number1 + number2)

print('The result is ', f(20, 30))
print('The result is ', f(40, 30))