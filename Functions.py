def find_total(exp):
    total  = 0
    for item in exp:
        total += item
    return total 
        
bharat_expenses = [20,45,30]
bharat_total = find_total(bharat_expenses)
kamal_expenses = [30,40,93]
kamal_total = find_total(kamal_expenses)
print(bharat_total)
print(kamal_total)
