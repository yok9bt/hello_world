num1 = 123
num2 = 232

def check_palindrom(n):
    # This function check if n is palindrom number. Parameter n should be integer. Function return True or Flase
    string_n = str(n)
    list_n = [*string_n]
    list_n_reverse = list_n.copy()
    list_n_reverse.reverse()
    if list_n==list_n_reverse: return True
    else: return False

print(check_palindrom(num1))
print(check_palindrom(num2))