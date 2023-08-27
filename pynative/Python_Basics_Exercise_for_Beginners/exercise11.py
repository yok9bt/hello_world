number = 5785434
list = [*str(number)]
list.reverse()
expected_string = ''
for x in list:
    expected_string += (x+' ')
print(expected_string)