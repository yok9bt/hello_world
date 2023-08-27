print('Oryginal String is :', end=' ')
oryginal_string = input()
print('Printing only even index chars')
for x in range(0, len(oryginal_string), 2):
    print(oryginal_string[x])