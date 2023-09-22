def print_pattern(n=5):
    for i in range(n):
        s= ''
    
    for j in range(i+1):
        s = s + '*'
        
    print(s)
    
print("Print pattern with input=3")
print_pattern(3)
print("Print pattern with input=4")
print_pattern(4)
print("Print pattern with no input number")
print_pattern() # Not supplying any input will use default argument which is 5
