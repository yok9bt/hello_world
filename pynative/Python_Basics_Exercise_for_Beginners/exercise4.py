
def modify_string(s, n):
    # This function return modified string, s parameter is a string, n parameter is number of removed first chars
    l = [*s]
    for x in range(n):
        l.pop(0)
    s=''
    for x in l:
        s+=x
    return s


def modify_string_v2(s, n):
    # This function return modified string, s parameter is a string, n parameter is number of removed first chars
    return s[n:]

oryginal_string = "hello_world"
print(oryginal_string)
print(modify_string(oryginal_string, 4))
print(modify_string_v2(oryginal_string, 2))
