income = 45000
tax = 0

# Firstly I calculate tax from last tax threshold 20% from income over 20 000$
surplus = max(0, income - 20000)
tax += surplus * 0.2
income -= surplus 
# Secondly I calculate tax from second tex threshold 10% from income over 10 000$
surplus = max(0, income - 10000)
tax += surplus * 0.1
income -= surplus

print(tax)