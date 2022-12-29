# 4  +  2  =  26 
# 8  +  1  =  79 
# 6  +  5  =  111
# 7  +  3  =  ???

def get_resultado(a, b):
    return str(a - b) + str(a + b)

def print_resultado(a, b):
    print(a, " + ", b, " = ", get_resultado(a, b))

print_resultado(4, 2)
print_resultado(8, 1)
print_resultado(6, 5)
print_resultado(7, 3)

# 4  +  2  =  26 
# 8  +  1  =  79 
# 6  +  5  =  111
# 7  +  3  =  410