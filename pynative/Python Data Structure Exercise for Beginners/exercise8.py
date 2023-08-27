roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
new_roll_number = []

for x in roll_number:
    if x in sample_dict.values():
        new_roll_number.append(x)
print(new_roll_number)

# I learn in this case that it is bad to remove element from list
#  during the going through that list in for loop!